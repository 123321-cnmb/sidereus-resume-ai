import json
import httpx
# 注意这里的导入路径适配了新的模块结构
from core.config import settings
from services.prompt_loader import PromptManager
from models.resume_models import ResumeAnalysisResult

class LLMAnalyzerEngine:
    def __init__(self):
        self.api_key = settings.MY_REAL_API_KEY
        self.base_url = settings.DEEPSEEK_BASE_URL
        self.prompt_manager = PromptManager()

    async def analyze(self, resume_text: str, job_desc: str) -> dict:
        system_prompt = self.prompt_manager.load("hr_analyzer")
        
        user_prompt = "【岗位需求】：\n{job_description}\n\n【简历内容】：\n{resume_content}".format(
            job_description=job_desc, 
            resume_content=resume_text[:10000]
        )

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.1
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            result = response.json()
        
        raw_content = result['choices'][0]['message']['content']
        parsed_data = json.loads(raw_content)
        
        validated_data = ResumeAnalysisResult(**parsed_data)
        return validated_data.dict()