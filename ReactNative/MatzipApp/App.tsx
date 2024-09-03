import {NavigationContainer} from '@react-navigation/native';
import React, {useState} from 'react';
import {
  Text,
  StyleSheet,
  TextInput,
  SafeAreaView,
  View,
  // Button,
  // View,
} from 'react-native';
import AuthStackNavigator from './src/navigation/AuthStackNavigator';

function App(): JSX.Element {
  const [name, setName] = useState('');

  const handleChangeInput = (text: string) => {
    console.log(text);
    setName(text);
  };

  return (
    <NavigationContainer>
      <AuthStackNavigator />
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },

  input: {
    flex: 1,
    borderWidth: 2,
    borderColor: 'black',
    height: 50,
    width: 100,
  },

  inputContainer: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
  },
});

export default App;
