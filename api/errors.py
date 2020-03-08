class InternalServerError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class CategoryAlreadyExistsError(Exception):
    pass


class ArticleRefersCategoryError(Exception):
    pass


class CategoryNotExistsError(Exception):
    pass


class ArticleAlreadyExistsError(Exception):
    pass


class ArticleNotExistsError(Exception):
    pass


class CreateOrModifyDateNotCanBeSet(Exception):
    pass


class InvalidAuthorization(Exception):
    pass


errors = {
    "InvalidId": {
        "message": "Invalid Id",
        "status": 400
    },
    "InternalServerError": {
        "message": "Internal Server Error",
        "status": 500
    },
    "InvalidSignatureError": {
        "message": "Invalid Signature Error",
        "status": 400
    },
    "ValidationError": {
        "message": "Validation error or missing required fields",
        "status": 400
    },
    "FieldDoesNotExist": {
        "message": "Fields do not exist on the document",
        "status": 400
    },
    "InvalidAuthorization": {
        "message": "Invalid Authorization",
        "status": 401
    },
    "EmailAlreadyExistsError": {
        "message": "Email already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid email or password",
        "status": 401
    },
    "NoAuthorizationError": {
        "message": "Missing Authorization Header",
        "status": 500
    },

    "CategoryAlreadyExistsError": {
        "message": "Category already exists",
        "status": 400
    },
    "ArticleRefersCategoryError": {
        "message": "Article.categories refers to it",
        "status": 400
    },
    "CategoryNotExistsError": {
        "message": "Category not exists",
        "status": 400
    },

    "ArticleAlreadyExistsError": {
        "message": "Name or link of article already exists",
        "status": 400
    },
    "ArticleNotExistsError": {
        "message": "Article not exists",
        "status": 400
    },
    "CreateOrModifyDateNotCanBeSet": {
        "message": "CreateDateTime or ModifyDateTime can`t be set, this is a automatic value",
        "status": 400
    }
}
