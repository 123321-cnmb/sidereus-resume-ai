from pydantic import BaseModel, Field
from typing import List

class CandidateInfo(BaseModel):
    name: str = Field(..., description="姓名")
    phone: str = Field(..., description="电话")
    email: str = Field(..., description="邮箱")
    address: str = Field(default="未提供", description="地址")
    job_intention: str = Field(default="未提供", description="求职意向")
    expected_salary: str = Field(default="未提供", description="期望薪资")
    work_years: str = Field(default="未提供", description="工作年限")
    education_bg: str = Field(default="未提供", description="学历背景")
    project_experience: List[str] = Field([], description="项目经历列表")

class ResumeAnalysisResult(BaseModel):
    candidate_info: CandidateInfo
    skills_match_rate: int = Field(..., description="技能匹配率")
    experience_relevance: int = Field(..., description="经验相关性")
    comprehensive_score: int = Field(..., description="综合评分")
    evaluation_reason: str = Field(..., description="HR 评价")