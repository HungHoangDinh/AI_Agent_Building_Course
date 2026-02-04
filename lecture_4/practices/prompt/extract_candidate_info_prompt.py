"""Prompt trích xuất thông tin ứng viên từ CV (FUNCTIONS.md mục 4).

TODO:
- Viết prompt hướng dẫn LLM đọc CV (`{cv_text}`) và trích xuất các trường:
  name, years_experience, skills, position, seniority, main_skills, domain, strengths.
- Yêu cầu LLM trả về **duy nhất một JSON object** khớp schema CandidateInfo
  (không giải thích thêm, không thêm text ngoài JSON).
- Tùy chỉnh nội dung prompt (tiếng Việt/Anh, giọng điệu, ví dụ...) theo nhu cầu của bạn.
"""

EXTRACT_CANDIDATE_INFO_PROMPT = """
TODO: Viết prompt trích xuất thông tin ứng viên từ CV (cv_text) và trả về JSON CandidateInfo.
"""

