from library.extension import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'username', 'password', 'address', 'phone')


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'adminname', 'password')


class Total_priceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'men_price', 'women_price',
                  'men_product', 'women_product', 'label')


class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content', 'username', 'id_pdf')


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'phone_ct', 'email_ct',
                  'user_ct', 'mess_ct', 'address_ct')


class Image_dataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pdf_url', 'name', 'type',
                  'school')
