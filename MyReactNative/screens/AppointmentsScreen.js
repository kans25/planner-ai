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
    <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Title"
           placeholderTextColor = "#808080"
           autoCapitalize = "none"
           onChangeText = {this.handleEmail}/>
        
        <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Location"
           placeholderTextColor = "#808080"
           autoCapitalize = "none"
           onChangeText = {this.handlePassword}/>

        <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Start Time"
           placeholderTextColor = "#808080"
           autoCapitalize = "none"
           onChangeText = {this.handlePassword}/>
        

        <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Deadline"
           placeholderTextColor = "#808080"
           autoCapitalize = "none"
           onChangeText = {this.handlePassword}/>
        
        <TextInput style = {styles.input}
           underlineColorAndroid = "transparent"
           placeholder = "Hours"
           placeholderTextColor = "#808080"
           autoCapitalize = "none"
           onChangeText = {this.handlePassword}/>

        <TextInput style = {styles.notes}
           underlineColorAndroid = "transparent"
           placeholder = "Notes"
           placeholderTextColor = "#808080"
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
     borderColor: '#1e90ff',
     borderWidth: 1
  },
  submitButton: {
     backgroundColor: '#1e90ff',
     padding: 10,
     margin: 15,
     height: 40,
  },
  submitButtonText:{
     color: 'white'
  },
  notes: {
    margin: 15,
    height: 65,
    borderColor: '#1e90ff',
    borderWidth: 1
 },
  imagestyle:{
     width: 80, 
     height: 80, 
     marginLeft: 140,
     justifyContent: 'center', 
     alignItems: 'center'
  }
})
