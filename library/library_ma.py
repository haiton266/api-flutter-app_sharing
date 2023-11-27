from library.extension import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'username', 'password', 'address', 'phone')


class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content', 'username', 'id_pdf')


class Image_dataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pdf_url', 'name', 'type',
                  'school', 'username')
