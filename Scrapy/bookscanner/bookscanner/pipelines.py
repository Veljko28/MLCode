from itemadapter import ItemAdapter
import mysql.connector

class BookscannerPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                if type(value) is tuple:
                    adapter[field_name] = value[0].strip()
                elif value is not None:
                    adapter[field_name] = value.strip()

        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()


        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            if type(value) is tuple:
                value[0] = value[0].replace('£', '')
                adapter[price_key] = float(value[0])
            elif value is not None:
                adapter[price_key] = float(value.replace('£', ''))


        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)

        stars_string = adapter.get('stars')
        split_stars_array = stars_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == 'zero':
            adapter['stars'] = 0
        elif stars_text_value == 'one':
            adapter['stars'] = 1
        elif stars_text_value == 'two':
            adapter['stars'] = 2
        elif stars_text_value == 'three':
            adapter['stars'] = 3
        elif stars_text_value == 'four':
            adapter['stars'] = 4
        elif stars_text_value == 'five':
            adapter['stars'] = 5

        return item


class SaveToMySqlPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='books'
        )

        self.cur = self.conn.cursor()


        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id int NOT NULL auto_increment,
                url VARCHAR(255),
                title text,
                upc VARCHAR(255),
                product_type VARCHAR(255),
                price_excl_tax DECIMAL,
                price_incl_tax DECIMAL,
                tax DECIMAL,
                price DECIMAL,
                availability INTEGER,
                num_reviews INTEGER,
                stars INTEGER,
                category VARCHAR(255),
                description text,
                PRIMARY KEY(id)
            )
        """)


    def process_item(self, item, spider):

        self.cur.execute(""" insert into books (
        url,title,upc,product_type,price_excl_tax,price_incl_tax,
        tax,price,availability,num_reviews,stars,category,description) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (item['url'], item['title'], item['upc'], item['product_type'], item['price_excl_tax'], item['price_incl_tax'], item['tax'],
        item['price'], item['availability'], item['num_reviews'], item['stars'], item['category'], str(item['description'][0])))

        self.conn.commit()
        return item


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
