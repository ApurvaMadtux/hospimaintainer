#contains databse logics and data related operations

from lib.db import connection


"""
CREATE TABLE customer_info
      (Customer_Name varchar2(255) NOT NULL,
        Customer_Id   varchar2(18) NOT NULL, 
       Open_Date  date NOT NULL,
       Last_Consulted_Date date,
       Vaccination_Id varchar2(5),
       Dr_Name varchar2(255),
       State varchar2(5) ,
        Country varchar2(5),
        post_code number(5),
        DOB date,
        Is_Active varchar(1) ,
        CONSTRAINT TEST_PK PRIMARY KEY (Customer_Name)
        )
   PARTITION BY LIST (Country)
      (PARTITION q_usa VALUES ('USA'),
       PARTITION q_ind VALUES ('IND'),
       PARTITION q_phil VALUES  ('PHIL'),
       PARTITION q_nyc VALUES ('NYC'),
       PARTITION q_au VALUES ('AU'));
"""



def create_table():
    try:

    except:
        print('An exception occurred')

