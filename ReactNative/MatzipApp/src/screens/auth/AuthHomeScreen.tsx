import {StackScreenProps} from '@react-navigation/stack';
import React from 'react';
import {StyleSheet, View, SafeAreaView, Text} from 'react-native';
import {AuthStackParamList} from '../../navigations/stack/AuthStackNavigator';
import {authNavigations} from '../../constants';
import CustomButton from '../../components/CustomButton';

type AuthHomeScreenProps = StackScreenProps<
  AuthStackParamList,
  typeof authNavigations.AUTH_HOME
>;

function AuthHomeScreen({navigation}: AuthHomeScreenProps) {
  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.container}>
        <Text style={styles.title}>MATZIP</Text>
        <View style={styles.buttonContainer}>
          <CustomButton
            label="로그인 하기"
            onPress={() => navigation.navigate(authNavigations.LOGIN)}
          />
          <CustomButton
            label="회원가입 하기"
            variant="outlined"
            onPress={() => navigation.navigate(authNavigations.SIGNUP)}
          />
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 40,
    textAlign: 'center',
    marginBottom: 200,
    fontWeight: 'bold',
  },
  buttonContainer: {
    width: '100%',
    alignItems: 'center',
  },
});

export default AuthHomeScreen;
