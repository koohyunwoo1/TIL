import React from 'react';
import {View, Text, Button, StyleSheet} from 'react-native';

function ModalScreen({navigation}) {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>This is a Modal!</Text>
      <Button title="Close Modal" onPress={() => navigation.goBack()} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  text: {
    fontSize: 24,
    marginBottom: 20,
  },
});

export default ModalScreen;
