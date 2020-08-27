from sqlalchemy import create_engine, Column, Integer, String  # crate_engine()方法用于创建数据库连接
from sqlalchemy.ext.declarative import declarative_base  # 导入基类,用于声明性系统映射
from sqlalchemy.orm import sessionmaker


# 建立sqlalchemy连接
engine = create_engine('mysql://root:kagura@localhost/sqlalchemy?charset=utf8', encoding='utf-8', echo=True)

# 申明映射
Base = declarative_base()


# 根据基类定义映射类
class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    full_name = Column(String(20))
    nick_name = Column(String(20))

    def __repr__(self):
        return "<User(name={}, fullname={}, nickname={})>".format(self.name, self.full_name, self.nick_name)


# 创建会话
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

if __name__ == '__main__':

    # 为数据表添加对象
    addUser = User(name='苦艾酒', full_name='王磊', nick_name='贝尔摩德')
    session.add(addUser)
    session.commit()
    session.close()


