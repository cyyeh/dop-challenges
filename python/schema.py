from pydantic import BaseModel


class BookItemData(BaseModel):
    isbn: str
    title: str
    publication_year: int
    author_ids: list[str]


class AuthorData(BaseModel):
    name: str
    book_isbns: list[str]


class CatalogData(BaseModel):
    books_by_isbn: dict[str, BookItemData]
    authors_by_id: dict[str, AuthorData]


class LibrarianData(BaseModel):
    email: str
    encrypted_password: str


class MemberData(BaseModel):
    email: str
    encrypted_password: str
    is_blocked: bool


class UserManagementData(BaseModel):
    librarians: dict[str, LibrarianData]
    members: dict[str, MemberData]


class LibraryData(BaseModel):
    name: str
    address: str
    catalog: CatalogData
    user_management: UserManagementData
