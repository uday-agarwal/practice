package com.practice.designpatterns.builder;

public class Response {
  private float likelihood;
  private int nextValue;
  private String whatToSay;

  public float getLikelihood() {
    return likelihood;
  }

  public int getNextValue() {
    return nextValue;
  }

  public String getWhatToSay() {
    return whatToSay;
  }

  // Nested static class for the builder.
  public static class Builder {
    private Response response;

    private Builder() {
      response = new Response();
    }

    public static Builder getBuilder() {
      return new Builder();
    }

    public Builder setLikelihood(float likelihood) {
      response.likelihood = likelihood;
      return this;
    }

    public Builder setNextValue(int nextValue) {
      response.nextValue = nextValue;
      return this;
    }

    public Builder setWhatToSay(String whatToSay) {
      response.whatToSay = whatToSay;
      return this;
    }

    public Response build() {
      return response;
    }
  }
}
