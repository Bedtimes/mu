from helper.database import db
from mu.model.entity.product import Product, ProductMedium, ProductType, ProductStatus

def add_product(product):
    db.session.add(product)
    db.session.commit()
    return product.product_id

def fetch_products(product_type=None):
    query = db.session.query(Product)
    products = query.all()
    return products

def fetch_product_types():
    query = db.session.query(ProductType)
    product_types = [(pt.product_type_id, pt.name) for pt in query.all()]
    return product_types

def fetch_product_statuses():
    query = db.session.query(ProductStatus)
    product_statuses = [(ps.product_status_id, ps.name) for ps in query.all()]
    return product_statuses

def fetch_product_mediums():
    query = db.session.query(ProductMedium)
    product_mediums = [(pm.product_medium_id, pm.name) for pm in query.all()]
    return product_mediums
