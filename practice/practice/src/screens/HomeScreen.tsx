import React from 'react';
import {View, Text, StyleSheet, Image} from 'react-native';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.greeting}>현우님 안녕하세요!</Text>
      <Text style={styles.subtitle}>오늘 영양제는 드셨나요?</Text>
      <View style={styles.imageContainer}>
        <Image source={require('../assets/Pill.png')} style={styles.image} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: 'white',
  },
  greeting: {
    fontSize: 40,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  subtitle: {
    fontSize: 18,
    marginBottom: 250,
    fontStyle: 'italic',
  },
  imageContainer: {
    width: 200,
    height: 200,
    justifyContent: 'center',
    alignItems: 'center',
  },
  image: {
    width: 200,
    height: 200,
  },
  // glow: {
  //   position: 'absolute',
  //   width: 250,
  //   height: 250,
  //   borderRadius: 125,
  //   backgroundColor: '#a4f87b',
  //   opacity: 0.5,
  //   elevation: 33,
  // },
});

export default HomeScreen;
