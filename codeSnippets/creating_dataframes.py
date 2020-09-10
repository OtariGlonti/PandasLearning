import pandas as pd

first_list_with_data = [
    {"name":"maria","gender":"female","date of birth":"1989-12-24","hight_cm":165},
    {"name":"marco","gender":"male","date of birth":"1991-10-01","hight_cm":181},
    {"name":"otto","gender":"male","date of birth":"1995-02-14","hight_cm":190},
    {"name":"lara","gender":"female","date of birth":"1965-01-01","hight_cm":173},
    {"name":"lisa","gender":"female","date of birth":"2000-06-03","hight_cm":185},

    {"name":"lorna","gender":"female","date of birth":"2000-10-12","hight_cm":175},
    {"name":"maccel","gender":"male","date of birth":"1993-11-11","hight_cm":191},
    {"name":"hans","gender":"male","date of birth":"1994-04-15","hight_cm":163},
    {"name":"lotti","gender":"female","date of birth":"1955-06-01","hight_cm":171},
    {"name":"anna","gender":"female","date of birth":"2001-04-02","hight_cm":155},

    {"name":"veronika","gender":"female","date of birth":"1992-06-20","hight_cm":155},
    {"name":"vincent","gender":"male","date of birth":"1995-10-02","hight_cm":176},
    {"name":"klaus","gender":"male","date of birth":"1991-07-17","hight_cm":198},
    {"name":"wanda","gender":"female","date of birth":"1985-11-22","hight_cm":169},
    {"name":"susi","gender":"female","date of birth":"2006-03-03","hight_cm":181},

    {"name":"paula","gender":"female","date of birth":"1987-02-14","hight_cm":166},
    {"name":"ulrich","gender":"male","date of birth":"1994-12-01","hight_cm":184},
    {"name":"alexander","gender":"male","date of birth":"1997-01-11","hight_cm":140},
    {"name":"dascha","gender":"female","date of birth":"1967-03-19","hight_cm":163},
    {"name":"kimi","gender":"female","date of birth":"2003-08-09","hight_cm":175}
    ]




people_data1 = pd.DataFrame(first_list_with_data)
#print(people_data1.groupby("gender")["hight_cm"].describe())
x = people_data1.groupby("gender").describe().apply(print)
print(x)
#print(x)

#test = people_data1[(people_data1["hight_cm"]>160) & (people_data1["gender"]=="female")]
#print(type(test))
#test2 = people_data1[people_data1["gender"]== "female"]
#print(test2)
#print(people_data1[people_data1["gender"]=="female" & people_data1["hight_cm"]>160])
#print(people_data1[people_data1["gender"]== "female"])
#people_data2 = pd.DataFrame(second_list_with_data)

#people_data1.to_csv("resources/people_data1.csv")
#people_data2.to_csv("resources/people_data2.csv")

#people_data1And2 = people_data1.append(people_data2)
#print(people_data1And2.reset_index(drop=True))


second_list_with_data = [
    {"name":"marta","gender":"female","date of birth":"1989-12-24","hight_cm":155},
    {"name":"Frank","gender":"male","date of birth":"1995-9-01","hight_cm":185},
    {"name":"Karl","gender":"male","date of birth":"1990-04-15","hight_cm":160},
    {"name":"Anna","gender":"female","date of birth":"1960-01-01","hight_cm":179},
    {"name":"Sophie","gender":"female","date of birth":"2001-05-03","hight_cm":195}]