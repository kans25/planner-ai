//import * as WebBrowser from 'expo-web-browser';
import React,{Component} from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  TextInput,
} from 'react-native';

import { MonoText } from '../components/StyledText';

class Inputs extends Component {
  state = {
     email: '',
     password: ''
  }
  handleEmail = (text) => {
     this.setState({ email: text })
  }
  handlePassword = (text) => {
     this.setState({ password: text })
  }
  login = (email, pass) => {
     alert('email: ' + email + ' password: ' + pass)
  }

  render() {
  return (
    <View style = {styles.container}>
       <Image
       source={require('../assets/images/googlelogo.png')}
       style={styles.imagestyle} 
    />
    <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Email"
           placeholderTextColor = "#000000"
           autoCapitalize = "none"
           onChangeText = {this.handleEmail}/>
        
        <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Password"
           placeholderTextColor = "#000000"
           autoCapitalize = "none"
           onChangeText = {this.handlePassword}/>
        
        <TouchableOpacity
           style = {styles.submitButton}
           onPress = {
              () => this.login(this.state.email, this.state.password)
           }>
           <Text style = {styles.submitButtonText}> Submit </Text>
        </TouchableOpacity>
     </View>
  )
}
}

export default Inputs

const styles = StyleSheet.create({
  container: {
     paddingTop: 23
  },
  input: {
     margin: 15,
     height: 40,
     borderColor: '#db3236',
     borderWidth: 1
  },
  submitButton: {
     backgroundColor: '#db3236',
     padding: 10,
     margin: 15,
     height: 40,
  },
  submitButtonText:{
     color: 'white'
  }, 
  imagestyle:{
     width: 80, 
     height: 80, 
     marginLeft: 140,
     justifyContent: 'center', 
     alignItems: 'center'
  }
})
