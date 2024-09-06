import React from 'react';
import {View, Text, StyleSheet, Image, FlatList} from 'react-native';

interface Supplement {
  id: string;
  name: string;
  image: any;
}

const supplements: Supplement[] = [
  {id: '1', name: '비타민 C', image: require('../assets/vitamin_c.png')},
  {id: '2', name: '오메가 3', image: require('../assets/omega_3.png')},
  {id: '3', name: '철분제', image: require('../assets/iron.png')},
];

const HomeScreen: React.FC = () => {
  const renderSupplement = ({item}: {item: Supplement}) => (
    <View style={styles.supplementItem}>
      <Image source={item.image} style={styles.supplementImage} />
      <Text style={styles.supplementName}>{item.name}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.greeting}>현우님 안녕하세요!</Text>
      <Text style={styles.subtitle}>오늘 영양제는 드셨나요?</Text>
      <View style={styles.imageContainer}>
        <Image source={require('../assets/Pill.png')} style={styles.image} />
        <View style={styles.bubble}>
          <FlatList
            data={supplements}
            renderItem={renderSupplement}
            keyExtractor={item => item.id}
            contentContainerStyle={styles.listContent}
            showsVerticalScrollIndicator={false}
          />
        </View>
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
    paddingTop: 60,
    width: 200,
    height: 200,
    justifyContent: 'center',
    alignItems: 'center',
    position: 'relative',
  },
  image: {
    width: 200,
    height: 200,
  },
  bubble: {
    position: 'absolute',
    top: -150,
    width: 300,
    height: 150,
    backgroundColor: '#ffffff',
    borderRadius: 20,
    padding: 10,
    borderWidth: 1,
    borderColor: 'black',
    overflow: 'hidden',
  },
  listContent: {
    flexGrow: 1,
    paddingBottom: 10,
  },
  supplementItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  supplementImage: {
    width: 50,
    height: 50,
    marginRight: 10,
  },
  supplementName: {
    fontSize: 16,
  },
});

export default HomeScreen;
