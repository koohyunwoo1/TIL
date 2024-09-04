import React, {useState} from 'react';
import {View, StyleSheet, Image} from 'react-native';
import {TextInput} from 'react-native-gesture-handler';

const SearchScreen = () => {
  const [text, setText] = useState('');
  const onChangeText = inputText => {
    setText(inputText);
  };

  return (
    <View style={styles.container}>
      <Image source={require('../assets/Pill2.png')} style={styles.img} />
      <TextInput
        onChangeText={onChangeText}
        value={text}
        placeholder="영양제를 검색하겠습니까?"
        style={styles.input}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  input: {
    width: '100%',
    maxWidth: 400,
    backgroundColor: 'lightgray',
    borderRadius: 10,
    paddingHorizontal: 20,
    height: 40,
    elevation: 8,
  },
  img: {
    width: 250,
    height: 80,
  },
});

export default SearchScreen;
