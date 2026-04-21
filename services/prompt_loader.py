import os
from pathlib import Path

class PromptManager:
    """负责从外部 Markdown 文件动态加载 System Prompt"""
    def __init__(self, prompts_dir: str = "prompts"):
        # 动态获取项目根目录，确保 Serverless 部署时也能找到 prompts 文件夹
        base_dir = Path(__file__).resolve().parent.parent
        self.prompts_dir = base_dir / prompts_dir

    def load(self, prompt_name: str) -> str:
        file_path = self.prompts_dir / f"{prompt_name}.md"
        if not file_path.exists():
            raise FileNotFoundError(f"⚠️ 提示词文件缺失: {file_path}")
        return file_path.read_text(encoding="utf-8")