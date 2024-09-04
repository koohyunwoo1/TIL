import React, {useEffect} from 'react';
import {View, StyleSheet, Image, ActivityIndicator} from 'react-native';
import {useNavigation} from '@react-navigation/native';

const WelcomeScreen = () => {
  const navigation = useNavigation();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigation.navigate('Login');
    }, 3000);

    return () => clearTimeout(timer);
  }, [navigation]);

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Image source={require('../assets/Logo.png')} style={styles.logo} />
        <ActivityIndicator
          size="large"
          color="#a4f87b"
          style={styles.spinner}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  content: {
    alignItems: 'center',
  },
  logo: {
    width: 600,
    height: undefined,
    aspectRatio: 1,
    resizeMode: 'contain',
  },
  spinner: {
    marginBottom: 10,
  },
});

export default WelcomeScreen;
