# Prompts cho Agent Phỏng vấn Nhân sự (FUNCTIONS.md mục 4)

# TODO: EXTRACT_CANDIDATE_INFO_PROMPT — trích xuất thông tin ứng viên trong 1 bước từ CV (text): name, years_experience, skills, position, seniority, main_skills, domain, strengths.
EXTRACT_CANDIDATE_INFO_PROMPT = """
"""

# TODO: GENERATE_QUESTIONS_PROMPT — sinh 3–5 câu hỏi phỏng vấn theo candidate_info (id, skill, question, max_score).
GENERATE_QUESTIONS_PROMPT = """
"""

# TODO: SCORE_ANSWER_PROMPT — chấm câu trả lời, trả về score + comment.
SCORE_ANSWER_PROMPT = """
"""

# TODO: FINAL_EVALUATION_PROMPT — level (Pass | Consider | Reject) + summary.
FINAL_EVALUATION_PROMPT = """
"""
