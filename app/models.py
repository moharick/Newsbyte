class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    Article class to define Article Objects
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):

        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
