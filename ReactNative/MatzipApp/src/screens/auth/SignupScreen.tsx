import React, {useRef} from 'react';
import {SafeAreaView, StyleSheet, Text, View} from 'react-native';
import InputField from '../../components/InputField';
import useForm from '../../hooks/useForm';
import CustomButton from '../../components/CustomButton';
import {validateSignup} from '../../utils';
import {TextInput} from 'react-native-gesture-handler';

function SignupHomeScreen() {
  const passwordRef = useRef<TextInput | null>(null);
  const passwordConfirmRef = useRef<TextInput | null>(null);

  const signup = useForm({
    initialValue: {email: '', password: '', passwordConfirm: ''},
    validate: validateSignup,
  });

  const handleSubmit = () => {
    console.log(signup.values);
  };
  return (
    <SafeAreaView style={styles.container}>
      {/* SafeAreaView ios나 Android 노치 같은 부분에 가려지는 
      것을 방지하고 만들어진 태그
      */}
      <View style={styles.inputContainer}>
        <InputField
          placeholder="이메일"
          error={signup.errors.email}
          touched={signup.touched.email}
          inputMode="email"
          returnKeyType="next"
          // 다음으로 가는 키보드의 키가 생긴다.
          blurOnSubmit={false}
          // 제출을 눌러도 키보드가 닫히지 않는다.
          onSubmitEditing={() => passwordRef.current?.focus()}
          {...signup.getTextInputProps('email')}
        />
        <InputField
          ref={passwordRef}
          placeholder="비밀번호"
          textContentType="oneTimeCode"
          error={signup.errors.password}
          touched={signup.touched.password}
          secureTextEntry
          returnKeyType="next"
          // 다음으로 가는 키보드의 키가 생긴다.
          blurOnSubmit={false}
          // 제출을 눌러도 키보드가 닫히지 않는다.
          {...signup.getTextInputProps('password')}
          onSubmitEditing={() => passwordConfirmRef.current?.focus()}
        />
        <InputField
          ref={passwordConfirmRef}
          placeholder="비밀번호"
          error={signup.errors.passwordConfirm}
          touched={signup.touched.passwordConfirm}
          secureTextEntry
          onSubmitEditing={handleSubmit}
          {...signup.getTextInputProps('passwordConfirm')}
        />
      </View>
      <CustomButton label="회원가입" onPress={handleSubmit} />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    margin: 30,
  },
  inputContainer: {
    gap: 20,
    marginBottom: 30,
  },
});

export default SignupHomeScreen;
