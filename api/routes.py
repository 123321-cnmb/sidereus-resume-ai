import os
import tempfile
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

# 引入核心配置和业务服务
from core.cache import CacheManager
from services.parser_service import ParserEngine
from services.llm_service import LLMAnalyzerEngine

router = APIRouter()
cache_mgr = CacheManager()
parser_engine = ParserEngine()
llm_engine = LLMAnalyzerEngine()

@router.post("/analyze")
async def analyze_endpoint(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    ext = Path(file.filename).suffix
    if ext.lower() != '.pdf':
        raise HTTPException(status_code=400, detail="目前仅支持 PDF 格式")

    content = await file.read()
    cache_key = cache_mgr.generate_key(content, job_description)
    
    cached_data = cache_mgr.get(cache_key)
    if cached_data:
        return {"source": "cache", "data": cached_data}

    sys_temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(sys_temp_dir, f"temp_{file.filename}")
    
    try:
        with open(temp_path, "wb") as f:
            f.write(content)
        
        resume_text = parser_engine.extract_text(temp_path, ext)
        analysis_result = await llm_engine.analyze(resume_text, job_description)
        
        cache_mgr.set(cache_key, analysis_result)
        return {"source": "ai_engine", "data": analysis_result}
        
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)