import React from 'react';
import {StyleSheet, View, Text} from 'react-native';

function App(): JSX.Element {
  return (
    <View style={styles.container}>
      <Text>텍스트</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'red',
  },
});

export default App;
