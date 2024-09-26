import mysql.connector
import requests
from datetime import date

# connection with database
Info = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "Fitness_Tracker"
)
cursor = Info.cursor()
def checkfood(food):
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {'Content-Type':'application/json', 'x-app-id':'cf603149', 'x-app-key':'cbbd0d41f6db22ef430c149072faa50a'}
    def get_data(q):
        try:
            data={
            "query":q,
            "timezone": "US/Eastern"
            }
            res=requests.post(url, headers=headers, json=data)
            n_data=[]
            for i in range(len(res.json()['foods'])):
                name=("Name-"+str(res.json()['foods'][i]['food_name']))
                qty=("Quantity-"+str(res.json()['foods'][i]['serving_qty']))
                serv=("Serving-"+str(res.json()['foods'][i]['serving_unit']))
                weight=("Weight-"+str(res.json()['foods'][i]['serving_weight_grams']))
                cal=("Calories-"+str(res.json()['foods'][i]['nf_calories']))
                fat=("Fats-"+str(res.json()['foods'][i]['nf_total_fat']))
                cho=("Cholesterol-"+str(res.json()['foods'][i]['nf_cholesterol']))
                carbs=("Carbs-"+str(res.json()['foods'][i]['nf_total_carbohydrate']))
                fiber=("Fiber-"+str(res.json()['foods'][i]['nf_dietary_fiber']))
                sugars=("Sugars-"+str(res.json()['foods'][i]['nf_sugars']))
                protein=("Protein-"+str(res.json()['foods'][i]['nf_protein']))
                n_data.append([name,qty,serv,weight,cal,fat,cho,carbs,fiber,sugars,protein])
            return n_data
        except:
            return False
    got_data=get_data(food)
    return got_data

def mealgenerate(calories,fat,carbs,protein,cuisine,diet):
    url = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=02622c97a85346999337fc44ff9ec008'
    headers = {'Content-Type':'application/json'}
    url = url + f'&maxCalories={calories}' + f'&maxFat={fat}' + f'&maxProtein={protein}' + f'&maxCarbs={carbs}' + f'&cuisine={cuisine}' + f'&diet={diet}'
    try:
        res = requests.get(url,headers=headers)
        return res.json()
    except:
        return False


def registerUser(data):
    try:
        cursor.execute('INSERT INTO `users` (`email`,`username`,`password`,`age`,`height`,`weight`,`gender`,`activity`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',data)
        Info.commit()
        return (True,)
    except Exception as e:
        return (False, e.args[1])
    

def loginUser(data):
    try:
        cursor.execute('SELECT * FROM `users` WHERE `username` = %s AND `password` = %s',data)
        return cursor.fetchone()
    except:
        return False
    
    
def updateval(data,weight):
    try:
        val = cursor.lastrowid
        data = list(data)
        data.append(val)
        data = tuple(data)
        cursor.execute('UPDATE `users` SET `weightgoal` = %s, `timegoal` = %s,`calorieperday` = %s,`fatperday` = %s,`carbsperday` = %s,`proteinperday` = %s WHERE `id` = %s',data)
        Info.commit()
        day = date.today()
        enterweight((val,weight,day))
        return True
    except Exception as e:
        print(e)
        return False
    

def fetchlastdetails():
    try:
        val = cursor.lastrowid
        cursor.execute('SELECT * FROM `users` WHERE `id` = %s',(val,))
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False


def provide_exercise():
    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
        "X-RapidAPI-Key":
        "d3919447fdmsh9ae39ea04397469p1567d9jsn033f132484d9",
        "X-RapidAPI-Host":
        "exercisedb.p.rapidapi.com"
    }

    response = requests.get(url,headers=headers)

    res = (response.json())
    return res

def gif_exercise(giflink):
    url = "https://youtube-search-and-download.p.rapidapi.com/channel/about"
    querystring = {giflink}
    headers = {
        "X-RapidAPI-Key":
        "d3919447fdmsh9ae39ea04397469p1567d9jsn033f132484d9",
        "X-RapidAPI-Host":
        "youtube-search-and-download.p.rapidapi.com"
    }
    response = requests.get(url,headers=headers,params=querystring)
    print(response.json())


def getAllTask():
    try:
        cursor.execute('SELECT * FROM `users`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False

       
def enterfood(data):
    try:
        for i in data:
            cursor.execute('INSERT INTO `meals` (`id`,`food`,`calories`,`fat`,`carbs`,`protein`,`mealtime`,`mealday`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',i)
            Info.commit()
            return True
    except Exception as e:
        print(e)
        return False
    

def fetchfood(data):
    try:
        cursor.execute('SELECT * FROM `meals` WHERE `id` = %s AND `mealtime` = %s',data)
        return cursor.fetchall()
    except Exception as e:
        return False
    
def checkdate(today):
    try:
        cursor.execute("SELECT * FROM `meals` WHERE `mealday` = %s",today)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
def fetchweight():
    try:
        cursor.execute("SELECT * FROM `weight_table`")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
def enterweight(data):
    try:
        cursor.execute('INSERT INTO `weight_table` (`id`,`weight`,`date`) VALUES (%s,%s,%s)',data)
        Info.commit()
    except Exception as e:
        print(e)
        return False
    
def notification():
    from plyer import notification
    notification.notify(
        title='Fitness Tracker',
        message='Its time to hydrate yourself',)