import React from 'react';
import {View, Image, StyleSheet, TouchableOpacity, Text} from 'react-native';
import {useNavigation} from '@react-navigation/native';
import {StackNavigationProp} from '@react-navigation/stack';

type AuthStackParamList = {
  Login: undefined;
  Main: undefined;
};

type LoginScreenNavigationProp = StackNavigationProp<
  AuthStackParamList,
  'Login'
>;

const LoginScreen = () => {
  const navigation = useNavigation<LoginScreenNavigationProp>();

  const handleLogin = () => {
    navigation.replace('Main');
  };

  return (
    <>
      <View>
        <Text style={styles.text}>영양제 추천을 받으러 가보실까요 ?</Text>
      </View>
      <View style={styles.container}>
        <TouchableOpacity onPress={handleLogin}>
          <Image source={require('../assets/kakao.png')} style={styles.image} />
          <Image
            source={require('../assets/naver.png')}
            style={[styles.image, styles.secondImage]}
          />
        </TouchableOpacity>
      </View>
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    paddingBottom: 100,
  },
  image: {
    width: 250,
    height: 60,
    resizeMode: 'stretch',
  },
  secondImage: {
    marginTop: 15,
  },
  text: {
    paddingTop: 200,
    textAlign: 'center',
    fontSize: 25,
    fontStyle: 'italic',
  },
});

export default LoginScreen;
