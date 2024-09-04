import React from 'react';
import {StyleSheet, View, Button, SafeAreaView} from 'react-native';

function AuthHomeScreen({navigation}) {
  return (
    <SafeAreaView>
      <View>
        <Button
          title="로그인 화면으로 이동"
          onPress={() => navigation.navigate('Login')}
        />
        <Button
          title="모달 오픈"
          onPress={() => navigation.navigate('MyModal')}
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({});

export default AuthHomeScreen;
