
<<<<<<< HEAD
from datetime import datetime

import psycopg2

# Connect & Query data from D.B
def connect_db(report_query):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(report_query)
    result_of_the_report = cursor.fetchall()
    conn.close()
    return result_of_the_report


# display the most popular 3 articles
def most_popular_three_articles():
    articles = connect_db("""select title, count(*) as total_page_views
             from articles, log
             where slug = substr(path, 10)
             group by title
             order by total_page_views desc
             limit 3;""")
    print("\n Most Popular Three Articals All Time: \n ")
    for title, total_page_views in articles:
        print(" \""+title+"\" -- "+str(total_page_views)+" views")


# display the most popular authors Desending
def most_popular_authors():
    authors = connect_db("""select name, count(*) as total_page_views
            from articles, authors, log
            where articles.author = authors.id
            and slug = substr(path, 10)
            group by name
            order by total_page_views desc;""")
    print("\n Most Popular Three Authors All Time: \n")
    for name, total_page_views in authors:
        print(" \""+name+"\" -- "+str(total_page_views)+" views")
    

# display the days did more than 1% of requests lead to error
def days_of_large_error_percent():
    errors_days = connect_db("""select * from (
                select all_visit.day,
                round(cast((100*faild_visit.requests) as numeric) / cast(all_visit.requests as numeric), 1)
                as error_percent from
                (select date(time) as day, count(*) as requests from log group by day) as all_visit
                join
                (select date(time) as day, count(*) as requests from log where status
                != '200 OK' group by day) as faild_visit
                on all_visit.day = faild_visit.day)
                as t where error_percent > 1.0;""")
    print("\n Days Of Error Percent More Than 1% : \n")
    for day, error_percent in errors_days:
        print(" "+datetime.strftime(day,'%b %d, %Y')+" -- "+str(error_percent)+"% errors")

                      

if __name__ == '__main__':
    most_popular_three_articles()
    most_popular_authors()
    days_of_large_error_percent()
=======
>>>>>>> b1e9f91b3d57bb7beb50176deb3dee9e391a9a19
