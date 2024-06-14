import openai

def summarize_text(api_key, text):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "あなたは会議の議事録を作成するアシスタントです。"},
            {"role": "user", "content": "これから会議の文字起こしの要点を抽出した文章を渡します。 この会議の要約、要点のリスト、決定事項のリスト、タスクのリストを返してください。"},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message["content"]