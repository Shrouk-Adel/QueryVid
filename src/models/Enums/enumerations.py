from enum import Enum


class ResponseSingal(Enum):
    WELCOM_MESSAGE="welcome to our system"
    FILE_TYPE_NOT_VALID ="file type not valid"
    FILE_SIZE_EXCEEDED='file type exeeded'
    FILE_UPLOADED_SUCCSESS ='file uploaded successfully'