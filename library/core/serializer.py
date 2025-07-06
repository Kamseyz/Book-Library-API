from rest_framework import serializers
from .models import Book, Category



#SERIALIZED CATEGORY
class SerializedCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
        
        
#CREATE CATEGORY
class CreateSerializedCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
     
    #create category   
    def create(self, validated_data):
        user = self.context['request'].user
        return Category.objects.create(user = user, **validated_data)
    
    #validate name length
    def validate(self, attrs):
        name = attrs.get('name')
        if len(name) < 3:
            raise serializers.ValidationError("Name must be more than 3 characters")
        elif len(name) > 50:
            raise serializers.ValidationError("Name cannot be greater than 50 characters")
        else:
            return attrs
        
    def validate_name(self,value):
        if Category.objects.filter(name = value).exists():
            raise serializers.ValidationError("Category already exist")
        return value



#UPDATE CATEGORY
class UpdateSerializedCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
     
    #instance and update category   
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    #validate the name category
    def validate(self, attrs):
        name = attrs.get('name')
        if len(name) < 3:
            raise serializers.ValidationError("Name must be more than 3 characters")
        elif len(name) > 50:
            raise serializers.ValidationError("Name cannot be greater than 50 characters")
        else:
            return attrs
        
   
#SERIALIZED BOOK    
class SerializedBook(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'author',
            'title',
            'book_file',
            'category',
        ]
        

#CREATE BOOK
class CreateSerializedBook(serializers.ModelSerializer):
    author = serializers.CharField(min_length =3, max_length = 100)
    title = serializers.CharField(min_length =3, max_length = 100)
    class Meta:
        model = Book
        fields = [
            'id',
            'author',
            'title',
            'book_file',
            'category',
            'posted_by',
        ]
    read_only_fields = [
        'category',
        'posted_by',
        'id'
    ]
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('posted_by', None)
        return Book.objects.create(posted_by = user, **validated_data)
    
    def validate_title(self,value):
        if Book.objects.filter(title = value).exists():
            raise serializers.ValidationError('Book title already exist')
        return value
    
    
#UPDATE BOOK
class UpdateSerializedBook(serializers.ModelSerializer):
    author = serializers.CharField(min_length =3, max_length = 100)
    title = serializers.CharField(min_length =3, max_length = 100)
    class Meta:
        model = Book
        fields = [
            'author',
            'title',
            'book_file',
            'category',
            'posted_by',
        ]
    read_only_fields = [
        'category',
        'posted_by',
    ]
    
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.book_file = validated_data.get('book_file', instance.book_file)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    def validate_title(self,value):
        if Book.objects.filter(title = value).exists():
            raise serializers.ValidationError('Book title already exist')
        return value