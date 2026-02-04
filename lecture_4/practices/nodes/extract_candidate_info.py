
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
from prompt import EXTRACT_CANDIDATE_INFO_PROMPT


class CandidateInfo(BaseModel):
    """Thông tin ứng viên trích xuất từ CV (1 bước). Các trường có thể rỗng nếu CV không cung cấp."""

    name: Optional[str] = Field(default=None, description="Họ tên ứng viên")
    years_experience: Optional[int] = Field(
        default=None, description="Số năm kinh nghiệm"
    )
    skills: Optional[list[str]] = Field(
        default=None, description="Danh sách kỹ năng"
    )
    position: Optional[str] = Field(default=None, description="Vị trí ứng tuyển")
    seniority: Optional[str] = Field(
        default=None,
        description="Bậc kinh nghiệm: Junior / Mid / Senior / Lead",
    )
    main_skills: Optional[list[str]] = Field(
        default=None, description="Kỹ năng chính"
    )
    domain: Optional[str] = Field(default=None, description="Lĩnh vực / domain")
    strengths: Optional[list[str]] = Field(default=None, description="Điểm mạnh")


def extract_candidate_info_node(state: dict) -> dict:
    """Input: cv_text. Output: candidate_info (dict từ CandidateInfo) hoặc error nếu lỗi."""

    try:
        cv_text = state.get("cv_text") or ""

        # TODO:
        # - Dùng OpenAI LLM để gọi model (theo config của bạn)
        # - Truyền vào prompt EXTRACT_CANDIDATE_INFO_PROMPT (format với cv_text)
        # - Yêu cầu model trả về JSON khớp schema CandidateInfo ở trên
        # - Parse JSON đó thành CandidateInfo(...) rồi:
        #       info = CandidateInfo(**json_data)
        #       return {"candidate_info": info.model_dump()}

        return {"candidate_info": {}}
    except Exception as e:
        return {"error": True, "error_message": str(e)}
