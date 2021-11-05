from wtforms import Form, StringField, TextAreaField

class AnnouncementForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    