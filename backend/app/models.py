from sqlalchemy import create_engine, Column, String, Integer, \
    ForeignKey, Float, DateTime, JSON, \
        LargeBinary, Numeric, Date, \
    TIMESTAMP, BigInteger

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import BYTEA
from datetime import datetime



Base = declarative_base()

# common
class User(Base):
    """User model."""
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    union_id = Column(String(255))
    openid = Column(String(255))
    name = Column(String(255))
    avatar = Column(String(255), default='avatar.jpg')
    subscribe_scene = Column(String(255))
    password = Column(String(255))
    phone_num = Column(String(20), unique=True)
    session_key = Column(String(255))
    vip_end_time = Column(DateTime)
    status = Column(Integer, default=1)
    register_time = Column(DateTime, default=func.now())
    user_info = Column(JSON, default={"usable_token": 20})
    email = Column(String(100), unique=True)
    referee = Column(UUID(as_uuid=True))
    ip = Column(String(45))

    files = relationship('File', back_populates='user')


class UserThirdPartyAccount(Base):
    __tablename__ = 'user_third_party_accounts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    third_party_name = Column(String(100), nullable=False)
    third_party_user_id = Column(String(255), nullable=False)
    additional_info = Column(JSONB)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())


class File(Base):
    __tablename__ = 'files'

    file_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(255), nullable=False)
    cloud_storage_identifier = Column(String(255))
    upload_time = Column(DateTime, default=func.now())
    file_size = Column(Integer)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'))
    group_id = Column(UUID(as_uuid=True))
    
    user = relationship('User', back_populates='files')


class FileContent(Base):
    __tablename__ = 'file_content'

    id = Column(String(64), primary_key=True)
    file_data = Column(LargeBinary)


class Image(Base):
    __tablename__ = 'images'

    id = Column(String(255), primary_key=True)
    image_data = Column(BYTEA, nullable=False)
    format = Column(String(20), nullable=False)
    source_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())


# Define the Plan, Discount, UserSubscription, Rebate, Order, and Withdrawal classes here

class Referral(Base):
    __tablename__ = 'referral'

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    referee_id = Column(UUID(as_uuid=True), nullable=False)
    rebate = Column(Float, default=0.0)


class Plan(Base):
    __tablename__ = 'plans'  # 表名应该与数据库中的名称匹配，注意大小写和引号

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    base_price = Column(Numeric, nullable=False)
    chat_limit = Column(Integer, nullable=False)
    store_limit = Column(Integer, nullable=False)
    expire_days = Column(Integer, default=30, nullable=False)
    daily_chat_count = Column(Integer, default=100, nullable=False)
    creatable_role_count = Column(Integer, default=5, nullable=False)
    creatable_knowledge_count = Column(Integer, default=5, nullable=False)

    def __repr__(self):
        return f"<Plan(name={self.name}, base_price={self.base_price}, chat_limit={self.chat_limit})>"


class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    period = Column(Integer, nullable=False)
    discount_percent = Column(Numeric, nullable=False)



class UserSubscription(Base):
    __tablename__ = 'user_subscriptions'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    period = Column(Integer, nullable=False)
    effective_price = Column(Numeric, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)



class Rebate(Base):
    __tablename__ = 'rebates'

    id = Column(Integer, primary_key=True)
    referrer_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    beneficiary_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    order_id = Column(BigInteger, ForeignKey('orders.order_id'), nullable=False)
    rebate_amount = Column(Numeric, nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(Date, default=datetime.utcnow, nullable=False)
    paid_at = Column(Date)

    # Relationships
    referrer = relationship("User", foreign_keys=[referrer_id])
    beneficiary = relationship("User", foreign_keys=[beneficiary_id])
    order = relationship("Order")



class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(BigInteger, primary_key=True)  # 主键
    user_id = Column(String(255), nullable=False)
    plan_id = Column(Integer, nullable=False)
    trade_type = Column(String(50), nullable=False)
    price = Column(Numeric, nullable=False)
    status = Column(String(50), default='unpaid', nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    pay_info = Column(JSONB, nullable=False)
    vip_end_time = Column(TIMESTAMP, nullable=False)



class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    withdrawal_id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False)
    requested_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True))
    response = Column(JSONB)  # Optional: stores JSON data for responses or errors


