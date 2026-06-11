class InquiryVO:
    def __init__(self, inquiry_id, user_id, title, content):
        self.inquiry_id = inquiry_id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.reply = "답변 대기 중"
