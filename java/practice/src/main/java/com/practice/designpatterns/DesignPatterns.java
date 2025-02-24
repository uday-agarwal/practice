package com.practice.designpatterns;

import com.practice.designpatterns.builder.Response;
import com.practice.designpatterns.command.Command;
import com.practice.designpatterns.command.Light;
import com.practice.designpatterns.command.LightOnCommand;
import com.practice.designpatterns.command.MacroCommand;
import com.practice.designpatterns.command.Stereo;
import com.practice.designpatterns.command.StereoOnCommand;
import com.practice.designpatterns.factory.AveragePluginFactory;
import com.practice.designpatterns.factory.GreatPluginFactory;
import com.practice.designpatterns.factory.Plugin;
import com.practice.designpatterns.factory.PluginFactory;
import com.practice.designpatterns.factory.PluginType;
import com.practice.designpatterns.observer.publisher.WeatherPublisher;
import com.practice.designpatterns.observer.subscriber.WeatherSubscriber;
import com.practice.designpatterns.singleton.SingletonEnum;
import com.practice.designpatterns.singleton.SingletonSingleThreaded;
import com.practice.designpatterns.singleton.SingletonWithDoubleCheckedLocking;
import com.practice.designpatterns.singleton.SingletonWithSynchronized;

public class DesignPatterns {
  public static void testDesignPatterns() {
    // singletonClient();

    // factoryClient(new AveragePluginFactory(), PluginType.NEW_PLUGIN);
    // factoryClient(new GreatPluginFactory(), PluginType.NEW_PLUGIN);

    // observerClient();

    // builderClient();

    commandClient();
  }

  private static void singletonClient() {
    SingletonSingleThreaded singleton = SingletonSingleThreaded.getSingleton();
    System.out.println(singleton.getProperty());

    SingletonWithSynchronized synchronizedSingleton = SingletonWithSynchronized.getInstance();
    System.out.println("Synchronized Singleton hashcode: " + synchronizedSingleton.hashCode());

    SingletonWithDoubleCheckedLocking dclSingleton = SingletonWithDoubleCheckedLocking.getInstance();
    System.out.println("DCL singleton hashcode: " + dclSingleton.hashCode());

    SingletonEnum enumSingleton = SingletonEnum.SINGLE_INSTANCE;
    System.out.println(enumSingleton.getProperty());
  }

  private static void factoryClient(PluginFactory factory, PluginType type) {
    System.out.println("Testing factory method pattern.");
    Plugin plugin = factory.createPlugin(type);
    plugin.play();
    plugin.stream();
  }

  // Observer pattern, using the Java Flow API.
  // Based on the reactive stream framework.
  private static void observerClient() {
    WeatherPublisher weatherPublisher = new WeatherPublisher();
    WeatherSubscriber subscriber = new WeatherSubscriber(weatherPublisher);
  }

  private static void builderClient() {
    Response.Builder builder = Response.Builder.getBuilder();
    Response response = builder.setLikelihood(0.05f)
        .setNextValue(5).setWhatToSay("You rock!").build();
    System.out.println(response.getWhatToSay());
  }

  private static void commandClient() {
    Light light = new Light();
    LightOnCommand turnOnLightCommand = new LightOnCommand(light);
    Stereo stereo = new Stereo();
    StereoOnCommand stereoOnCommand = new StereoOnCommand(stereo);

    turnOnLightCommand.execute();
    stereoOnCommand.execute();

    MacroCommand macroCommand = new MacroCommand(new Command[] { turnOnLightCommand, stereoOnCommand });
    macroCommand.undo();
  }
}
