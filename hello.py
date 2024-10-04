import { Text, SafeAreaView, StyleSheet } from 'react-native';

// You can import supported modules from npm
import { Card } from 'react-native-paper';


import { Image } from 'react-native';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Card>
        <Text style={styles.paragraph}>
          Hello word
        </Text>
        <Image source={{ uri: 'https://imgs.search.brave.com/tN_VLXBlFtZW0c6s2h9tSd5yywtlHvi0BHB4rAeZSiY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuZ2VuaWFsbHku/Y29tL3MzZnMtcHVi/bGljL0ltYWdlJTIw/bGElMjB2aWxsZSUy/MGF1eCUyMG4lQzMl/QTlvbnNmci5wbmc_/VmVyc2lvbklkPXp2/bHBXcmU0aGdydW9W/RVYwM09sRjdkdTMx/ak5HRXcx' }} style={styles.image}/>
      </Card>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
    image: {
    width: 150,  
    height: 150, 
    alignSelf: 'center', 
    marginTop: 10, 
    marginBottom: 20,
  },
});
