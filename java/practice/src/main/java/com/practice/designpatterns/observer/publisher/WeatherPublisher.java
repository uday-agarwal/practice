package com.practice.designpatterns.observer.publisher;

import java.util.Objects;
import java.util.concurrent.Flow;

public class WeatherPublisher implements Flow.Publisher<WeatherData> {
  private WeatherData data;

  public WeatherPublisher() {
    data = new WeatherData();
  }

  @Override
  public void subscribe(Flow.Subscriber<? super WeatherData> subscriber) {
    if (Objects.isNull(subscriber)) {
      throw new NullPointerException("subscriber is null");
    }
    System.out.println("Producer: subscribing " + subscriber.getClass().getSimpleName());

    WeatherSubscription subscription = new WeatherSubscription(this, subscriber);
    subscriber.onSubscribe(subscription);
  }

  public void getCurrentWeatherData(Flow.Subscriber<? super WeatherData> subscriber) {
    subscriber.onNext(data);
  }
}
