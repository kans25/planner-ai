import React from 'react';
import { Platform } from 'react-native';
import { createStackNavigator, createBottomTabNavigator } from 'react-navigation';

import TabBarIcon from '../components/TabBarIcon';
import HomeScreen from '../screens/HomeScreen';
//import LinksScreen from '../screens/LinksScreen';
//import SettingsScreen from '../screens/SettingsScreen';
import InputsScreen from    '../screens/InputsScreen'
import AppointmentsScreen from '../screens/AppointmentsScreen'

const config = Platform.select({
  web: { headerMode: 'screen' },
  default: {},
});

const HomeStack = createStackNavigator(
  {
    Home: HomeScreen,
  },
  config
);

HomeStack.navigationOptions = {
  tabBarLabel: 'Home',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon
      focused={focused}
      name={
        Platform.OS === 'ios'
          ? `ios-information-circle${focused ? '' : '-outline'}`
          : 'md-information-circle'
      }
    />
  ),
};

HomeStack.path = '';

/*const LinksStack = createStackNavigator(
  {
    Links: LinksScreen,
  },
  config
);

LinksStack.navigationOptions = {
  tabBarLabel: 'Links',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon focused={focused} name={Platform.OS === 'ios' ? 'ios-link' : 'md-link'} />
  ),
};

LinksStack.path = '';
*/

/*
const SettingsStack = createStackNavigator(
  {
    Settings: SettingsScreen,
  },
  config
);

SettingsStack.navigationOptions = {
  tabBarLabel: 'Settings',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon focused={focused} name={Platform.OS === 'ios' ? 'ios-options' : 'md-options'} />
  ),
};

SettingsStack.path = '';
*/ 

const InputsStack = createStackNavigator(
  {
    Inputs: InputsScreen,
  },
  config
);

InputsStack.navigationOptions = {
  tabBarLabel: 'Inputs',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon focused={focused} name={Platform.OS === 'ios' ? 'ios-options' : 'md-options'} />
  ),
};

InputsStack.path = '';

const AppointmentsStack = createStackNavigator(
  {
    Appointments: AppointmentsScreen,
  },
  config
);

AppointmentsStack.navigationOptions = {
  tabBarLabel: 'Appointments',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon focused={focused} name={Platform.OS === 'ios' ? 'ios-options' : 'md-options'} />
  ),
};

AppointmentsStack.path = '';

const tabNavigator = createBottomTabNavigator({
  HomeStack,
  //LinksStack,
  //SettingsStack,
  InputsStack,
  AppointmentsStack,
});

tabNavigator.path = '';

export default tabNavigator;
