## dJango+공공데이터 Json 파일

#### 목표 : kakaomap API를 이용하여 json 데이터 올려주기

![image-20210216173135404](C:\Users\ajgkw\AppData\Roaming\Typora\typora-user-images\image-20210216173135404.png)



### json 파일 확인하기

https://www.data.go.kr/data/15013115/standard.do

다음 공공데이터 포털에서 Json 파일 형식으로 가져다 썼습니다.

```json
{"fields":
 [{"id":"충전소명"},{"id":"충전소위치상세"},{"id":"설치시도명"},{"id":"휴점일"},{"id":"이용가능시작시각"},{"id":"이용가능종료시각"},{"id":"완속충전가능여부"},{"id":"완속충전가능여부"},{"id":"급속충전타입구분"},{"id":"완속충전기대수"},{"id":"급속충전기대수"},{"id":"주차료부과여부"},{"id":"소재지도로명주소"},{"id":"소재지지번주소"},{"id":"관리업체명"},{"id":"관리업체전화번호"},{"id":"위도"},{"id":"경도"},{"id":"데이터기준일자"},{"id":"제공기관코드"},{"id":"제공기관명"}],
"records":[{"충전소명":"평촌목련신동아아파트","충전소위치상세":"경기도 안양시 동안구 동안로 75 (호계동, 목련신동아아파트) 301동,901동~903동","설치시도명":"경기도","휴점일":"-","이용가능시작시각":"00:00","이용가능종료시각":"24:00","완속충전가능여부":"Y","급속충전가능여부":"N","급속충전타입구분":"AC완속","완속충전기대수":"1","급속충전기대수":"0","주차료부과여부":"N","소재지도로명주소":"경기도 안양시 동안구 동안로 75 (호계동, 목련신동아아파트) 301동,901동~903동","소재지지번주소":"-","관리업체명":"케이티","관리업체전화번호":"1522-0123","위도":"37.38537331","경도":"126.953171","데이터기준일자":"2020-08-11","제공기관코드":"3830000","제공기관명":"경기도 안양시"}
           .........
```

다음과 같은 형식으로 들어와 있는 데이터에서 위도,경도,주소 등을 가져와 보는 걸 목표로 했다.



1. 📁EVapp/views.py

   

   **🎁👀전체코드**

   ```python
   def map(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + 'EVdata.json', encoding='utf-8') as json_file:
     attractions = json.load(json_file)['records']
     attractiondict = []
     for attraction in attractions:
      content = {
       "title": attraction['충전소명'],
       "mapx": attraction['경도'],
       "mapy": attraction['위도'],
       "addr": str(attraction['충전소위치상세']),
       "fee": attraction['주차료부과여부'],
       "starttime": str(attraction['이용가능시작시각']),
       "endtime": str(attraction['이용가능종료시각']),
       "slowYN": attraction['완속충전가능여부'],
       "fastYN": attraction['급속충전가능여부'],
      }
      if attraction.get('급속충전타입구분'):
       content['fasttype'] = str(attraction['급속충전타입구분'])
      else:
       content['fasttype'] = ''
      attractiondict.append(content)
     attractionJson = json.dumps(attractiondict, ensure_ascii=False)  
    return render(request, 'EVapp/map.html', {'attractionJson': attractionJson})
   ```

   

   * 파일경로를 가져와 오픈하는 코드

     ```python
     dir_path = os.path.dirname(os.path.realpath(__file__))
     with open(dir_path + '/' + 'EVdata.json', encoding='utf-8') as json_file:
     ```

   * json에서 필요한 데이터 경로를 확인하여, attractions에 담아주는 코드

     ```python
     attractions = json.load(json_file)['records']
     ```

     

   * 반복문을 돌려 필요한 위도 경도 이름 위치 등을 Content에 담는 코드

     ```python
     for attraction in attractions:
        content = {
         "title": attraction['충전소명'],
         "mapx": attraction['경도'],
         "mapy": attraction['위도'],
         "addr": str(attraction['충전소위치상세']),
         "fee": attraction['주차료부과여부'],
         "starttime": str(attraction['이용가능시작시각']),
         "endtime": str(attraction['이용가능종료시각']),
         "slowYN": attraction['완속충전가능여부'],
         "fastYN": attraction['급속충전가능여부'],
        }
     ```

     

   * json 객체 들 중에서 필요한 데이터만 가져오는 조건 코드

     ```python
     if attraction.get('급속충전타입구분'):
         content['fasttype'] = str(attraction['급속충전타입구분'])
        else:
         content['fasttype'] = ''
        attractiondict.append(content)
     ```

     

     🐣 *중간에 print(python)  / console.log(js)를 찍어보며 확인 해보면 됩니다.* 🐣

-------



### Json으로 받은 값 지도에 띄워주기

* #### 지도 생성 

  📁static/ js/ map.js

  ```javascript
  var mapContainer = document.getElementById('map'), // 지도를 표시할 div
  mapOption = {
      center: new kakao.maps.LatLng(37.56682, 126.97865), // 지도의 중심좌표
      level: 8, // 지도의 확대 레벨
      mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
  };
  
  // 지도를 생성한다
  var map = new kakao.maps.Map(mapContainer, mapOption);
  ```

  📁templates/ EVapp/ map.html

  ```html
  <body>
  <div id="map" style="width:100%;height:350px;"></div>
  
  <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=발급받은 APP KEY를 사용하세요"></script>
  ```



* #### json 에서 받아온 값을 수정 + 마크 표시

  📁templates/EVapp/map.html

  ```html
  <script>
      var attractions = JSON.parse("{{ attractionJson|escapejs }}");
  	console.log(attractions)
  </script>
  ```

  

  📁static/ js/ map.js

  ```python
  function mapdata(attractions) {
    for (var i = 0; i < Object.keys(attractions).length; i++) {
      //주차료 여부에 따라 바꾸기
      if(attractions[i].fee == "Y" || attractions[i].fee == "y"){
        attractions[i].fee = "주차료 有"
      }
      if(attractions[i].fee == "N" || attractions[i].fee == "n"){
        attractions[i].fee = "주차료 없음"
      }
  
      //완속 충전 여부에 따라 바꾸기
      if(attractions[i].slowYN == "Y"){
        attractions[i].slowYN = "완속충전 가능 O"
      }
      if(attractions[i].slowYN == "N"){
        attractions[i].slowYN = " "
      }
  
      //급속 충전 여부에 따라 바꾸기
      if(attractions[i].fastYN == "Y"){
        attractions[i].fastYN = "급속충전 가능 O"
      }
      if(attractions[i].fastYN == "N"){
        attractions[i].fastYN = " "
      }
      
    var content = {
          title: attractions[i].title,
          latlng: new kakao.maps.LatLng(attractions[i].mapy, attractions[i].mapx),
          addr: attractions[i].addr,
  
          starttime: attractions[i].starttime,
          endtime: attractions[i].endtime,
          fee: attractions[i].fee,
          slowYN: attractions[i].slowYN,
          fastYN: attractions[i].fastYN,
          fasttype: attractions[i].fasttype,
          }
          positions.push(content);
      }
  };
  
  // 마커 이미지의 이미지 주소입니다
  var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
  for (var i = 0; i < positions.length; i++) {
      // 마커 이미지의 이미지 크기 입니다
      var imageSize = new kakao.maps.Size(24, 35);
      // 마커 이미지를 생성합니다
      var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
      // 마커를 생성합니다
      var marker = new kakao.maps.Marker({
          map: map, // 마커를 표시할 지도
          position: positions[i].latlng, // 마커를 표시할 위치
          title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
          image: markerImage // 마커 이미지
      });
      markers.push(marker);
  
  ```

  

* #### 마크 클릭시 상세정보 띄우는 오버레이 생성

  📁static/ js/ map.js

  ```javascript
  (function(marker, place) {
      // 마크 클릭 시
      //console.log(typeof place.addr);
  
      kakao.maps.event.addListener(marker, 'click', function() {
        var overlay = new kakao.maps.CustomOverlay({
  
          // 오버레이에 띄울 내용
          content: '<div class="wrap">' +
                '    <div class="info">' +
                '        <div class="title">' +
                    place.title + '<div class="close" onclick="closeOverlay()" title="닫기"></div>' +
                '        </div>' +
                '        <div class="body">' +
                '                <div class="fee">' + place.fee + '</div>' +
                '            <div class="img">' +
                '                <img src= "../../static/img/kakaoMap.png" width="73" height="70">' +
                '           </div>' +
                '            <div class="desc">' +
                '                <div class="ellipsis">' + place.addr + '</div>' +
                '		         <div class="jibun ellipsis"> 운영 시간 : ' + place.starttime +'<span> - </span>' + place.endtime + '</div>' +
                '                <div class="ellipsis"> >'+ place.slowYN +  place.fastYN + '</div>' +
                '                <div class="ellipsis">'+ place.fasttype + '</div>' +
                '            </div>' +
                '        </div>' +
                '    </div>' +
                '</div>',
          map: map,
          position: marker.getPosition()
        });
  
        // 커스텀 오버레이를 닫기 위해 호출되는 함수입니다
        function closeOverlay() {
            overlay.setMap(null);
        }
  
        // 아무데나 클릭하게되면 overlay를 끄기
        kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
          overlay.setMap(null)
        })
  
        overlay.setMap(map);
      })
    })(marker, positions[i])
    }
  }
  ```

  

* #### 현위치 가져오는 코드

  ```javascript
  // 지도를 생성한다
  var map = new kakao.maps.Map(mapContainer, mapOption);
  
  // HTML5의 geolocation으로 사용할 수 있는지 확인합니다
  if (navigator.geolocation) {
      // GeoLocation을 이용해서 접속 위치를 얻어옵니다
      navigator.geolocation.getCurrentPosition(function(position) {
  
          var lat = position.coords.latitude, // 위도
              lon = position.coords.longitude; // 경도
  
          var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
              message = '<div style="padding:5px;">현재 위치</div>'; // 인포윈도우에 표시될 내용입니다
  
          // 마커와 인포윈도우를 표시합니다
          displayMarker(locPosition, message);
        });
  
  } else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
  
      var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
          message = 'geolocation을 사용할수 없어요..'
          displayMarker(locPosition, message);
  }
  
  // 지도에 마커와 인포윈도우를 표시하는 함수입니다
  function displayMarker(locPosition, message) {
  
      // 마커를 생성합니다
      var marker = new kakao.maps.Marker({
          map: map,
          position: locPosition
      });
  
      var iwContent = message, // 인포윈도우에 표시할 내용
          iwRemoveable = true;
  
      // 인포윈도우를 생성합니다
      var infowindow = new kakao.maps.InfoWindow({
          map: map,
          content : iwContent,
          removable : iwRemoveable
      });
  
      // 인포윈도우를 마커위에 표시합니다
      kakao.maps.event.addListener(marker, 'click', function() {
          infowindow.open(map, marker);
      });
  
      // 지도 중심좌표를 접속위치로 변경합니다
      map.setCenter(locPosition);
  }
  ```

  



**🎁👀전체코드**

📁static/ js/ map.js

```javascript
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
mapOption = {
    center: new kakao.maps.LatLng(37.56682, 126.97865), // 지도의 중심좌표
    level: 8, // 지도의 확대 레벨
    mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
};

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);

// HTML5의 geolocation으로 사용할 수 있는지 확인합니다
if (navigator.geolocation) {
    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function(position) {

        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도

        var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
            message = '<div style="padding:5px;">현재 위치</div>'; // 인포윈도우에 표시될 내용입니다

        // 마커와 인포윈도우를 표시합니다
        displayMarker(locPosition, message);
      });

} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

    var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
        message = 'geolocation을 사용할수 없어요..'
        displayMarker(locPosition, message);
}

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: locPosition
    });

    var iwContent = message, // 인포윈도우에 표시할 내용
        iwRemoveable = true;

    // 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        map: map,
        content : iwContent,
        removable : iwRemoveable
    });

    // 인포윈도우를 마커위에 표시합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
    });

    // 지도 중심좌표를 접속위치로 변경합니다
    map.setCenter(locPosition);
}

//--------------------------------------------가져온 json 파일 올리는 부분-----------------------------------------------

function mapdata(attractions) {
  for (var i = 0; i < Object.keys(attractions).length; i++) {
    //주차료 여부에 따라 바꾸기
    if(attractions[i].fee == "Y" || attractions[i].fee == "y"){
      attractions[i].fee = "주차료 有"
    }
    if(attractions[i].fee == "N" || attractions[i].fee == "n"){
      attractions[i].fee = "주차료 없음"
    }

    //완속 충전 여부에 따라 바꾸기
    if(attractions[i].slowYN == "Y"){
      attractions[i].slowYN = "완속충전 가능 O"
    }
    if(attractions[i].slowYN == "N"){
      attractions[i].slowYN = " "
    }

    //급속 충전 여부에 따라 바꾸기
    if(attractions[i].fastYN == "Y"){
      attractions[i].fastYN = "급속충전 가능 O"
    }
    if(attractions[i].fastYN == "N"){
      attractions[i].fastYN = " "
    }
    
  var content = {
        title: attractions[i].title,
        latlng: new kakao.maps.LatLng(attractions[i].mapy, attractions[i].mapx),
        addr: attractions[i].addr,

        starttime: attractions[i].starttime,
        endtime: attractions[i].endtime,
        fee: attractions[i].fee,
        slowYN: attractions[i].slowYN,
        fastYN: attractions[i].fastYN,
        fasttype: attractions[i].fasttype,
        }
        positions.push(content);
    }
    drawMap();
};
  //console.log(positions);

function drawMap(){
// 마커 이미지의 이미지 주소입니다
  var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
  for (var i = 0; i < positions.length; i++) {
    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: positions[i].latlng, // 마커를 표시할 위치
      title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      image: markerImage // 마커 이미지
    });
    markers.push(marker);

  (function(marker, place) {
    // 마크 클릭 시
    //console.log(typeof place.addr);

    kakao.maps.event.addListener(marker, 'click', function() {
      var overlay = new kakao.maps.CustomOverlay({

        // 오버레이에 띄울 내용
        content: '<div class="wrap">' +
              '    <div class="info">' +
              '        <div class="title">' +
                  place.title + '<div class="close" onclick="closeOverlay()" title="닫기"></div>' +
              '        </div>' +
              '        <div class="body">' +
              '                <div class="fee">' + place.fee + '</div>' +
              '            <div class="img">' +
              '                <img src= "../../static/img/kakaoMap.png" width="73" height="70">' +
              '           </div>' +
              '            <div class="desc">' +
              '                <div class="ellipsis">' + place.addr + '</div>' +
              '		         <div class="jibun ellipsis"> 운영 시간 : ' + place.starttime +'<span> - </span>' + place.endtime + '</div>' +
              '                <div class="ellipsis"> >'+ place.slowYN +  place.fastYN + '</div>' +
              '                <div class="ellipsis">'+ place.fasttype + '</div>' +
              '            </div>' +
              '        </div>' +
              '    </div>' +
              '</div>',
        map: map,
        position: marker.getPosition()
      });

      // 커스텀 오버레이를 닫기 위해 호출되는 함수입니다
      function closeOverlay() {
          overlay.setMap(null);
      }

      // 아무데나 클릭하게되면 overlay를 끄기
      kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
        overlay.setMap(null)
      })

      overlay.setMap(map);
    })
  })(marker, positions[i])
  }
}
```



