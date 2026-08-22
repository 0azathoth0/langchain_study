from ..PromptTemplates import *


class PromptLibrary:
    """
    存储所有可复用的提示词模板
    """

    # 导师角色模板（TUTOR）
    # 支持 subject(主题), level(难度/详细程度), question(具体问题)
    TUTOR = ChatPromptTemplate.from_messages([
        (
            "system",
            "你是一位精通 {subject} 领域的资深专家导师。"
            "请以 {level} 级别的深度（high为详尽深入，low为简洁明了）回答用户的问题。"
            "回答必须专业、准确，且使用中文。"
        ),
        ("human", "{question}")
    ])

    # 如果你以后还想加别的模板，比如代码审查、翻译等，可以继续添加：
    # CODE_REVIEW = ChatPromptTemplate.from_messages([...])