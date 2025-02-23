package com.practice.designpatterns.observer.publisher;

public class WeatherData {
  private int firstProperty;
  private String secondProperty = new String();

  public int getFirstProperty() {
    return firstProperty++;
  }

  public String getSecondProperty() {
    secondProperty += "Hell! ";
    return secondProperty;
  }
}
