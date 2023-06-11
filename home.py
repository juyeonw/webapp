import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image

with st.sidebar:#사이드바에 제목 기입
    st.subheader(':rice: 밥메뉴 정해주는 프로그램')
    
add_selectbox = st.sidebar.selectbox(#사이드바에 목차,'메뉴고르기'페이지와'지역 배달 차트'페이지로 분류
    "목차",
    ("메뉴 고르기", "지역 배달 차트","업종별 배달 차트","후기 및 소감")
)
with st.sidebar:#사이드바에 학번 이름 기입
    st.caption('made by.2103766우주연')

if(add_selectbox == "메뉴 고르기"):#사이드바에서 메뉴고르기 선택 시
    st.write('# :cherry_blossom: Welcome to My Web page!')
    st.warning('혹시, 밥 메뉴가 고민이신가요? 그렇다면, 이 웹앱을 이용해보세요!  생각하지 못했던 메뉴들을 추천해드릴게요.', icon="💡") #문구삽입(warning이 노란색이라 웹앱과 잘 어울릴 것 같아 정보 대신 사용)
    st.video('https://youtu.be/Pyr4HUpT1tg') #유튜브 실행
    st.caption('노래를 들으며 메뉴를 고민해보아요:ok_hand:')
    #여러개 선택해서 그중에서 랜덤으로 꼽아서 하나 추천 해 주는 프로그램
    genre = st.radio( #식사 시간을 선택
        ":stopwatch: 식사 시간을 정해주세요",
        ('아침', '점심', '저녁','술안주')) 
    st.divider() #가독성을 위해 분할선 
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
        st.warning('여기서 선택한 특징 중 한가지가 랜덤으로 정해져요! 정한 특징들의 교집합으로 결과가 나오는게 아니니 주의하세요.', icon="💡") #문구삽입
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
                
            st.write(':point_down: 데이터베이스에 저장된',randomchoicemenu,'리스트') 
            st.write(foods) #menu에 있는 것 중 choicemenu된 모든 데이터를 보여줌
            
            st.divider() #가독성을 위해 분할선 
            st.warning('위의 리스트에서 딱 한가지를 추천해 드릴게요! 특징을 하나만 선택해도 가능해요.', icon="💡") #문구삽입
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
    
    tab1, tab2 = st.tabs(["이용 여부", "월 평균 비용"]) #탭으로 이용 여부 데이터와 월 평균 비용 데이터를 나눔

    with tab1: #tab1 이용 여부인 경우
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

        st.write('지역에 따른 배달앱 이용 여부 년도별 변화 (%)')
        col1, col2 = st.columns([1, 3]) #좌측에 데이터 우측에 그래프 배치1:3비율로 
        with col1:#좌측
            st.write(usedataindex)#배달앱 이용자 백분율 데이터 배치 
        with col2:#우측
            df = pd.DataFrame(usedataindex)#pandas data frame으로 배달앱 이용자 백분율 데이터 변경
            st.line_chart(df) #라인차트 작성
            
    

    with tab2: #tab2 월 평균 비용인 경우
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
    
    st.divider() #가독성을 위해 분할선 
    st.write('업종에 따른 배달앱 이용 여부 년도별 변화 (%)')
    col1, col2 = st.columns([2, 5]) #좌측에 데이터 우측에 그래프 배치1:3비율로 
    with col1:#좌측
        st.write(Sydataindex)#배달앱 이용자 백분율 데이터 배치 
    with col2:#우측
        Sydf = pd.DataFrame(Sydataindex)#pandas data frame으로 배달앱 이용자 백분율 데이터 변경
        st.line_chart(Sydf) #라인차트 작성

if(add_selectbox == "후기 및 소감"):#사이드바에서 후기 및 소감 선택 시
    st.write("# :books: Reviews and impressions")
    st.write("streamlit module을 이용한 Web App 만들기 소감")
    tab1, tab2 = st.tabs(["소감", "제외된 기능들"]) #탭으로 이용 여부 데이터와 월 평균 비용 데이터를 나눔

    with tab1: #tab1 소감인 경우
        col1, col2 = st.columns([1, 4])#1:4비율로 좌측에 데이터 우측에 그래프 배치
        with col1:  #좌측
            image = Image.open('20230217_125702.jpg') #증명사진 불러오기
            st.image(image) #증명사진 띄우기
        with col2:      #우측
            st.write(" 안녕하세요! 저는 동아대학교에 재학중인 전자공학과 3학년 2103766 우주연입니다. 저는 이번에 '스마트 모빌리티 프로그래밍'이라는 과목을 수강하며, 이렇게 streamlit을 이용하여 저만의 웹앱을 만들게 되었습니다. streamlit을 이용하면 Python지식이 크지 않아도 저만의 웹앱을 구성할 수 있어 흥미로웠고 정말 재미있었습니다.")
            st.write(" 저도 밥 메뉴를 잘 고르지 못하는 편인데, 자주 보는 유튜브 채널'티키틱'에 업로드 된 '뭐먹을지 고민될때 부르는 노래'에서 영감을 받아 '밥메뉴 정해주는 프로그램'을 구상하게 되었습니다. 처음 구상했던 기능들에서 많은 것이 제외되어서 개인적으로 많은 아쉬움이 남습니다. 만약 Python을 더 공부하게 된다면, 원래 넣고자 했던 기능들을 더 추가하고 싶어요!")
        st.write(":heart: 이상으로 발표를 마치겠습니다:heart: ")
        if st.button('들어주셔서 감사합니다!'): #들어주셔서 감사합니다!를 클릭 시
            st.balloons() #풍선
    with tab2: #tab2 제외된 기능들인 경우, 실패한 기능들을 넣고싶어 작성하였습니다!
        st.write("1. 원래는 multiselect 기능에 text_input 기능으로 사용자에게 입력을 받아 랜덤 특징 선택에 원하는 카테고리를 추가할 수 있게끔 설계를 하였는데, 스트림릿은 입력이 바뀔때마다 계속해서 페이지가 새로고침되며 input이 초기화되어버려서, list로 구현하기 힘들다고 판단하여 제외하게 되었습니다. ")
        inputtext=st.text_input('텍스트를 입력하면 multiselect에 추가돼요!', '') #input을 받으면 inputtext애 추가
        options = st.multiselect( #inputtext가 한번만 추가되는 멀티셀렉트
    '',
    ['특징A', '특징B',inputtext],
    ['특징A', '특징B'])
        st.divider() #가독성을 위해 분할선 
        st.write("2. 선택한 특징에 대해 오늘의 추천 교집합 기능 추가")
        options = st.multiselect( #선택한 특징들을 options에 list로 저장
            ':game_die: 랜덤으로 선택하고 싶은 특징을 골라주세요',
            ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','고기','차가운 것','뜨거운 것'],
            ['한식', '중식','일식','양식','매운 것','안매운 것','밥','떡','면','빵','고기','차가운 것','뜨거운 것'])
        st.write("이부분은 처음 웹앱을 제작하면서 생각하지 않았던 방향인데, 주변 친구들에게 사전조사를 진행하니 멀티셀렉트에 담긴 특징들을 바탕으로 메뉴를 추천해주는 줄 알았다고 하는 의견이 있었습니다. 시간이 된다면 꼭 추가하고 싶습니다!")
        st.divider() #가독성을 위해 분할선 
        st.write("3. 산점도를 이용하여 지역별 차트와 관련된 부분을 더 가독성 있게 만들고 싶었으나, 데이터 가공 지식이 부족하여 어려움을 겪고 포기하게 되었습니다 :sob:")
        df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.66, 127.0], #산점도를 한국 지도 위에 띄우는 dataframe생성
        columns=['lat', 'lon'])
        st.map(df) #data frame을 바탕으로 map출력
        