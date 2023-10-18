# # 强调必须按照示例里的格式返回 
# # Complex issue: Yes or No 
PLANNER_PROMPT_CN = """请按照程序代码的逻辑,将复杂问题拆分成(2个或3个)子任务,非复杂问题无需拆分,确保有充分的信息以解决问题,严格按照以下格式返回：\n
``` 
Complex issue: Yes or No 
Subtask: 当前要解决的问题
Subtask: 当前要解决的问题
```\n
{EXAMPLES}
现在开始回答这个任务或者问题。请直接回答这个问题,不要包含其他不需要的文字。
问题：{question}\n
"""

EXAMPLES = """为了帮助你解决接下来的任务或者问题,我们提供了一些相关的示例。\n
问题:杜兰特进入NBA多少年了,年份的三次方是多少？ 
```
Complex issue: Yes
Subtask: 搜杜兰特进入NBA的开始年份,标记为 year1
Subtask: 获取当前是哪一年,标记为 year2
Subtask: 计算 (year2 - year1 ) ^ 3 数值
```\n
问题:介绍一下李白这个诗人？ 
```
Complex issue: No
```\n
问题:Craigslist的创始人何时出生
```
Complex issue: Yes
Subtask: 确定Craigslist的创始人是谁, 标记为 X
Subtask: 查找 X 的出生日期
```\n
""" 

CALL_PROTOCOL_CN = """你是一个问答助手,需要回答要解决任务或者问题。为了帮助你，我们提供此问题的来源（原问题）和额外的知识（参考信息）。注意其中一些参考信息可能存在噪声或无效信息，因此你需要谨慎的使用它们。\n
原问题：{origin_question}\n
参考信息：{reference_information}\n
现在开始回答这个任务或者问题。请直接回答这个问题，不要包含其他不需要的文字。{sub_question}\n
"""
