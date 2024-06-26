import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://testuser:testpass@localhost:5432/orders'
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:test@localhost:5432/order_test'
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}