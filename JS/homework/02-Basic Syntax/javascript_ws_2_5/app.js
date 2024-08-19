const citiesInfo = [
  {
    city: '서울',
    utcOffset: ['한국 표준시', 'KST', 'UTC+9'],
    latitude: 37,
    longitude: 126
  },
  {
    city: '도쿄',
    utcOffset: ['일본 표준시', 'JST', 'UTC+9'],
    latitude: 35,
    longitude: 139
  },
  {
    city: '상하이',
    utcOffset: ['중국 표준시', 'CST', 'UTC+8'],
    latitude: 31,
    longitude: 121
  }
]


for (let i = 0; i < citiesInfo.length; i++) {
  const city = citiesInfo[i]
  for (const key of Object.keys(city)) {
      const value = city[key]
    if ( key === 'city' ) {
      console.log(`수도 : ${value}`)
    }else {
      const valueType = Array.isArray(value) ? value[value.length - 1] : value
      // value가 배열이면 value[value.length - 1] 반환
      // 아니면 value를 그대로 반환한다.
      console.log(`${key}: ${valueType}`)
    }
  }


  console.log('')
}


