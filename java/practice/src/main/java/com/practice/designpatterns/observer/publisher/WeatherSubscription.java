package com.practice.designpatterns.observer.publisher;

import java.util.concurrent.Flow;

public class WeatherSubscription implements Flow.Subscription {
  private WeatherPublisher publisher;
  private Flow.Subscriber<? super WeatherData> subscriber;
  private int demand;

  public WeatherSubscription(WeatherPublisher publisher, Flow.Subscriber<? super WeatherData> subscriber) {
    this.publisher = publisher;
    this.subscriber = subscriber;
  }

  @Override
  public void request(long n) {
    demand += n;
    while (demand > 0) {
      demand--;
      publisher.getCurrentWeatherData(subscriber);
    }
  }

  @Override
  public void cancel() {
    demand = 0;
  }
}
