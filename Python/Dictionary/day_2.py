from loguru import logger

Labour_with_cost = {"Mahesh":500
                    ,"Ramesh":400
                    ,"Mithlesh":400
                    ,"Jagmohan":1000
                    ,"Sumesh":300
                    ,"Rampyare":800}

#most used tarika in real time
new_dict={
    "Shyam":600
    ,"Sundar":900
    ,"Sachivji":1000
}

final_dict={**Labour_with_cost,**new_dict}
logger.info(final_dict)

#Dictionary Comprehension
increment_dict={key:final_dict.get(key)+100 for key in final_dict}
logger.info(final_dict)
logger.info(increment_dict)

increment_dict = {
    key: final_dict.get(key, 0) + 500
    for key in final_dict
    if final_dict.get(key, 0) < 700
}

final_dict = {
    key: final_dict.get(key, 0) + 1
    if key!="Sachivji"
    else final_dict.get(key)
    for key in final_dict
}
print(final_dict)