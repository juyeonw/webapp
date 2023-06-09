import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

add_selectbox = st.sidebar.selectbox(#사이드바에 목차,'메뉴고르기'페이지와'지역 배달 차트'페이지로 분류
    "목차",
    ("메뉴 고르기", "지역 배달 차트","업종별 배달 차트")
)
with st.sidebar:#사이드바에 학번 이름 기입
    st.caption('made by.2103766우주연')

if(add_selectbox == "메뉴 고르기"):#사이드바에서 메뉴고르기 선택 시
    st.write('# :cherry_blossom: Welcome to My Web page!')
    st.video('https://youtu.be/Pyr4HUpT1tg') #유튜브 실행
    st.caption('노래를 들으며 메뉴를 고민해보아요:ok_hand:')
    #여러개 선택해서 그중에서 랜덤으로 꼽아서 하나 추천 해 주는 프로그램
    genre = st.radio( #식사 시간을 선택
        ":stopwatch: 식사 시간을 정해주세요",
        ('아침', '점심', '저녁','술안주')) 
    if genre=='술안주': #식사 시간에서 만약 술안주를 선택했다면
        if st.button('Dice!'): #Dice 버튼을 누를 시
            st.balloons()
            foods=['삼겹살','치킨','김치찌개','오징어/마른안주','과일','회','곱창/막창','두부김치','파전','골뱅이'] #foods에 대표적인 술안주 저장
            commendfood=foods[random.randrange(len(foods))] #foods에서 랜덤으로 한 메뉴 선택
            st.write('오늘 ',genre,'로 ',commendfood,' 은(는) 어떠세요?') #랜덤으로 선택된 메뉴를 추천
    else: #식사 시간에서 아침,점심,저녁을 선택했다면
        options = st.multiselect( #선택한 특징들을 options에 list로 저장
            ':game_die: 랜덤으로 선택하고 싶은 특징을 골라주세요',
            ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','고기','차가운 것','뜨거운 것'],
            ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','고기','차가운 것','뜨거운 것'])
        st.write('당신이 선택한 특징들:',options) #multiselect에서 고른 특징들을 보여줌
        
        if st.button('Dice!'): #Dice 버튼을 누를 시
            st.balloons()
            menudata=pd.read_csv('menu.csv',encoding='cp949') #menudata에 menu.csv파일 불러옴
            randomchoice=random.randrange(len(options)) #list의 갯수만큼 랜덤한 숫자 한가지를 선택
            randomchoicemenu=options[randomchoice] #그 숫자에 해당하는 options특징을 저장
            
            st.write('**랜덤으로 선택된 특징은:blue[*',randomchoicemenu,'*]입니다!**') #랜덤으로 특징을 추천하듯 출력됨
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
            elif randomchoicemenu=='고기': #만약 고기가 나온다면 
                foods=menudata[menudata['category'] == '고기']#foods에 고기 데이터를 저장
            elif randomchoicemenu=='뜨거운 것': #만약 뜨거운 것이 나온다면 
                foods=menudata[menudata['temp'] == '뜨거운 것']#foods에 뜨거운 것 데이터를 저장
            else: #만약 차가운 것이 나온다면 
                foods=menudata[menudata['temp'] == '차가운 것']#foods에 차가운 것 데이터를 저장
                
            st.write(':point_down:저장된',randomchoicemenu,'리스트') 
            st.write(foods) #menu에 있는 것 중 choicemenu된 모든 데이터를 보여줌
            
            Recommendone=foods.sample(n=1) #random으로 선택된 메뉴 속 데이터 중 하나를 선택
            Recommendonename=(Recommendone['name']) #하나의 데이터의 이름만 추출
            st.subheader(':yum: 오늘의 추천') #랜덤으로 선택된 메뉴의 한가지를 추천하는 문구 출력
            st.write('오늘의 ',genre,'으로 이건 어때요?') #랜덤으로 선택된 메뉴의 한가지를 추천하는 문구 출력
            st.write(Recommendonename) #랜덤으로 선택된 메뉴의 한가지를 추천
        
if(add_selectbox == "지역 배달 차트"):#사이드바에서 지역 배달 차트 선택 시
    st.write("# :bar_chart: Let's see the stats#1")
    st.subheader('지역에 따른 년도별 배달 변화 추이')#지역에 따른 배달 이용률 변화 추이
    data = pd.read_csv('delivery.csv',encoding='cp949') #delivery차트 파일을 읽어옴(출처:https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114054_016)
    year = st.slider(':spiral_calendar_pad:년도를 선택하세요.', 2018, 2022,2021)#슬라이더로 년도 선택 
    st.write(year,"년으로 보여드릴게요!")#선택한 년도 알려줌
    
    regiondata=data[data['특성별(1)']=='지역별'] #지역별로 된 데이터만 가져옴
    if year==2018:#만약 슬라이더가 2018이면
        usedata=regiondata[['특성별(2)','2018']] #지역이름과 2018년 데이터만 가져옴
        usedata['2018'] = pd.to_numeric(usedata['2018'], errors='coerce') #pd.to_numeric()= '2018' 열의 값을 숫자 유형으로 변환
        usedata.sort_values('2018', inplace=True) #오름차순으로 정렬
    elif year==2019:#만약 슬라이더가 2019이면
        usedata=regiondata[['특성별(2)','2019']]#지역이름과 2019년 데이터만 가져옴
        usedata['2019'] = pd.to_numeric(usedata['2019'], errors='coerce') #pd.to_numeric()= '2019' 열의 값을 숫자 유형으로 변환
        usedata.sort_values('2019', inplace=True) #오름차순으로 정렬
    elif year==2020:#만약 슬라이더가 2020이면
        usedata=regiondata[['특성별(2)','2020']]#지역이름과 2020년 데이터만 가져옴
        usedata['2020'] = pd.to_numeric(usedata['2020'], errors='coerce') #pd.to_numeric()= '2020' 열의 값을 숫자 유형으로 변환
        usedata.sort_values('2020', inplace=True) #오름차순으로 정렬
    elif year==2021:#만약 슬라이더가 2021이면
        usedata=regiondata[['특성별(2)','2021']]   #지역이름과 2021년 데이터만 가져옴
        usedata['2021'] = pd.to_numeric(usedata['2021'], errors='coerce') #pd.to_numeric()= '2021' 열의 값을 숫자 유형으로 변환
        usedata.sort_values('2021', inplace=True) #오름차순으로 정렬
    elif year==2022:#만약 슬라이더가 2022이면
        usedata=regiondata[['특성별(2)','2022']]#지역이름과 2022년 데이터만 가져옴
        usedata['2022'] = pd.to_numeric(usedata['2022'], errors='coerce') #pd.to_numeric()= '2022' 열의 값을 숫자 유형으로 변환
        usedata.sort_values('2022', inplace=True) #오름차순으로 정렬
    usedataindex=usedata.set_index('특성별(2)')#좌측의 숫자가 적힌 순서index를 지역으로 변경

    if year==2018:#만약 슬라이더가 2018이면
        dataprice=regiondata[['특성별(2)','2018.1']]#지역이름과 2018년 총 금액 데이터만 가져옴
        dataprice['2018.1'] = pd.to_numeric(dataprice['2018.1'], errors='coerce') #pd.to_numeric()= '2018.1' 열의 값을 숫자 유형으로 변환
        dataprice.sort_values('2018.1', inplace=True) #오름차순으로 정렬
    elif year==2019:#만약 슬라이더가 2019이면
        dataprice=regiondata[['특성별(2)','2019.1']]#지역이름과 2019년 총 금액 데이터만 가져옴
        dataprice['2019.1'] = pd.to_numeric(dataprice['2019.1'], errors='coerce') #pd.to_numeric()= '2019.1' 열의 값을 숫자 유형으로 변환
        dataprice.sort_values('2019.1', inplace=True) #오름차순으로 정렬
    elif year==2020:#만약 슬라이더가 2020이면
        dataprice=regiondata[['특성별(2)','2020.1']]#지역이름과 2020년 총 금액 데이터만 가져옴
        dataprice['2020.1'] = pd.to_numeric(dataprice['2020.1'], errors='coerce') #pd.to_numeric()= '2020.1' 열의 값을 숫자 유형으로 변환
        dataprice.sort_values('2020.1', inplace=True) #오름차순으로 정렬
    elif year==2021:#만약 슬라이더가 2021이면
        dataprice=regiondata[['특성별(2)','2021.1']]   #지역이름과 2021년 총 금액 데이터만 가져옴
        dataprice['2021.1'] = pd.to_numeric(dataprice['2021.1'], errors='coerce') #pd.to_numeric()= '2021.1' 열의 값을 숫자 유형으로 변환
        dataprice.sort_values('2021.1', inplace=True) #오름차순으로 정렬
    elif year==2022:#만약 슬라이더가 2022이면
        dataprice=regiondata[['특성별(2)','2022.1']]#지역이름과 2022년 총 금액 데이터만 가져옴
        dataprice['2022.1'] = pd.to_numeric(dataprice['2022.1'], errors='coerce') #pd.to_numeric()= '2022.1' 열의 값을 숫자 유형으로 변환
        dataprice.sort_values('2022.1', inplace=True) #오름차순으로 정렬
    datapriceindex=dataprice.set_index('특성별(2)')#좌측의 숫자가 적힌 순서index를 지역으로 변경

    st.write('지역에 따른 배달앱 이용 여부 년도별 변화 (%)')
    col1, col2 = st.columns([1, 3]) #좌측에 데이터 우측에 그래프 배치1:3비율로 
    with col1:#좌측
        st.write(usedataindex)#배달앱 이용자 백분율 데이터 배치 
    with col2:#우측
        df = pd.DataFrame(usedataindex)#pandas data frame으로 배달앱 이용자 백분율 데이터 변경
        st.line_chart(df) #라인차트 작성
    st.write('지역에 따른 배달앱 월 평균 비용 년도별 변화 (￦)')
    col1, col2 = st.columns([1, 3])#1:3비율로 좌측에 데이터 우측에 그래프 배치
    with col1:  #좌측
            st.write(datapriceindex)#배달앱 이용자별 한달 평균 이용 금액 데이터 배치
    with col2:      #우측
        df1 = pd.DataFrame(datapriceindex)#pandas data frame으로 배달앱 이용자별 한달 평균 이용 금액 데이터 변경
        st.line_chart(df1)#라인차트 작성
        
        
if(add_selectbox == "업종별 배달 차트"):#사이드바에서 업종별 배달 차트 선택 시
    st.write("# :bar_chart: Let's see the stats#2")
    st.subheader('업종에 따른 년도별 배달 변화 추이')#업종에 따른 배달 이용률 변화 추이
    year = st.slider(':spiral_calendar_pad:년도를 선택하세요.', 2018, 2022,2021)#슬라이더로 년도 선택 
    st.write(year,"년으로 보여드릴게요!")#선택한 년도 알려줌

    data = pd.read_csv('delivery.csv',encoding='cp949') #delivery차트 파일을 읽어옴(출처:https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114054_016)
    Sectorsdata=data[data['특성별(1)']=='업종별'] #업종별로 된 데이터만 가져옴
    if year==2018:#만약 슬라이더가 2018이면
        Sydata=Sectorsdata[['특성별(3)','2018']] #업종과 2018년 데이터만 가져옴
        Sydata['2018'] = pd.to_numeric(Sydata['2018'], errors='coerce') #pd.to_numeric()= '2018' 열의 값을 숫자 유형으로 변환
        Sydata.sort_values('2018', inplace=True) #오름차순으로 정렬
    elif year==2019:#만약 슬라이더가 2019이면
        Sydata=Sectorsdata[['특성별(3)','2019']]#업종과 2019년 데이터만 가져옴
        Sydata['2019'] = pd.to_numeric(Sydata['2019'], errors='coerce') #pd.to_numeric()= '2019' 열의 값을 숫자 유형으로 변환
        Sydata.sort_values('2019', inplace=True) #오름차순으로 정렬
    elif year==2020:#만약 슬라이더가 2020이면
        Sydata=Sectorsdata[['특성별(3)','2020']]#업종과 2020년 데이터만 가져옴
        Sydata['2020'] = pd.to_numeric(Sydata['2020'], errors='coerce') #pd.to_numeric()= '2020' 열의 값을 숫자 유형으로 변환
        Sydata.sort_values('2020', inplace=True) #오름차순으로 정렬
    elif year==2021:#만약 슬라이더가 2021이면
        Sydata=Sectorsdata[['특성별(3)','2021']]   #업종과 2021년 데이터만 가져옴
        Sydata['2021'] = pd.to_numeric(Sydata['2021'], errors='coerce') #pd.to_numeric()= '2021' 열의 값을 숫자 유형으로 변환
        Sydata.sort_values('2021', inplace=True) #오름차순으로 정렬
    elif year==2022:#만약 슬라이더가 2022이면
        Sydata=Sectorsdata[['특성별(3)','2022']]#업종과 2022년 데이터만 가져옴
        Sydata['2022'] = pd.to_numeric(Sydata['2022'], errors='coerce') #pd.to_numeric()= '2022' 열의 값을 숫자 유형으로 변환
        Sydata.sort_values('2022', inplace=True) #오름차순으로 정렬
    Sydataindex=Sydata.set_index('특성별(3)')#좌측의 숫자가 적힌 순서index를 지역으로 변경
    
    st.write('업종에 따른 배달앱 이용 여부 년도별 변화 (%)')
    col1, col2 = st.columns([2, 5]) #좌측에 데이터 우측에 그래프 배치1:3비율로 
    with col1:#좌측
        st.write(Sydataindex)#배달앱 이용자 백분율 데이터 배치 
    with col2:#우측
        Sydf = pd.DataFrame(Sydataindex)#pandas data frame으로 배달앱 이용자 백분율 데이터 변경
        st.line_chart(Sydf) #라인차트 작성

    


    
