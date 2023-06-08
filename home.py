import streamlit as st
import pandas as pd
import numpy as np
import random

data = pd.read_csv('delivery.csv',encoding='cp949')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
st.write(data)

#여러개 선택해서 그중에서 랜덤으로 꼽아서 하나 추천 해 주는 프로그램
genre = st.radio( #식사 시간을 선택
    "식사 시간을 정해주세요",
    ('아침', '점심', '저녁','술안주')) 
if genre=='술안주': #식사 시간에서 만약 술안주를 선택했다면
    if st.button('Dice!'): #Dice 버튼을 누를 시
        foods=['삼겹살','치킨','김치찌개','오징어/마른안주','과일','회','곱창/막창','두부김치','파전','골뱅이'] #foods에 대표적인 술안주 저장
        commendfood=foods[random.randrange(len(foods))] #foods에서 랜덤으로 한 메뉴 선택
        st.write('오늘 ',genre,'로 ',commendfood,' 은(는) 어떠세요?') #랜덤으로 선택된 메뉴를 추천
else: #식사 시간에서 아침,점심,저녁을 선택했다면
    options = st.multiselect( #선택한 특징들을 options에 list로 저장
        '랜덤으로 선택하고 싶은 특징을 골라주세요',
        ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','차가운 것','뜨거운 것'],
        ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','차가운 것','뜨거운 것'])
    st.write('당신이 선택한 특징들:',options) #multiselect에서 고른 특징들을 보여줌
    
    if st.button('Dice!'): #Dice 버튼을 누를 시
        menudata=pd.read_csv('menu.csv',encoding='cp949') #menudata에 menu.csv파일 불러옴
        randomchoice=random.randrange(len(options)) #list의 갯수만큼 랜덤한 숫자 한가지를 선택
        randomchoicemenu=options[randomchoice] #그 숫자에 해당하는 options특징을 저장
        
        st.write('랜덤으로 선택된 메뉴는',randomchoicemenu,'입니다') #랜덤으로 특징을 추천하듯 출력됨
        if randomchoicemenu=='한식': #만약 한식이 나온다면 
            foods=menudata[menudata['country'] == '한식'] #foods에 한식 데이터를 저장
        elif randomchoicemenu=='중식': #만약 중식이 나온다면 
            foods=menudata[menudata['country'] == '중식']#foods에 중식 데이터를 저장
        elif randomchoicemenu=='일식': #만약 일식이 나온다면 
            foods=menudata[menudata['country'] == '일식']#foods에 일식 데이터를 저장
        elif randomchoicemenu=='양식': #만약 양식이 나온다면 
            foods=menudata[menudata['country'] == '양식']#foods에 양식 데이터를 저장
        elif randomchoicemenu=='매운 것': #만약 매운 것이 나온다면 
            foods=menudata[menudata['mapgi'] == '매운 것']#foods에 매운 것 데이터를 저장
        elif randomchoicemenu=='안매운 것': #만약 안매운 것이 나온다면 
            foods=menudata[menudata['mapgi'] == '안매운 것']#foods에 안매운 것 데이터를 저장
        elif randomchoicemenu=='밥': #만약 밥이 나온다면 
            foods=menudata[menudata['category'] == '밥']#foods에 밥 데이터를 저장
        elif randomchoicemenu=='떡': #만약 떡이 나온다면 
            foods=menudata[menudata['category'] == '떡']#foods에 떡 데이터를 저장
        elif randomchoicemenu=='면': #만약 면이 나온다면 
            foods=menudata[menudata['category'] == '면']#foods에 면 데이터를 저장
        elif randomchoicemenu=='빵': #만약 빵이 나온다면 
            foods=menudata[menudata['category'] == '빵']#foods에 빵 데이터를 저장
        elif randomchoicemenu=='뜨거운 것': #만약 뜨거운 것이 나온다면 
            foods=menudata[menudata['temp'] == '뜨거운 것']#foods에 뜨거운 것 데이터를 저장
        else: #만약 차가운 것이 나온다면 
            foods=menudata[menudata['temp'] == '차가운 것']#foods에 차가운 것 데이터를 저장
            
        st.write('저장된',randomchoicemenu,'리스트') 
        st.write(foods) #menu에 있는 것 중 choicemenu된 모든 데이터를 보여줌
        
        choiceone=foods.sample(n=1) #choicemenu된 데이터 중 하나를 선택
        choiceonename=(choiceone['name']) #하나의 데이터의 이름만 추출
        
        st.write('오늘 ',genre,'으로 ',choiceonename,' 은(는) 어떠세요?') #랜덤으로 선택된 메뉴의 한가지를 추천
        
        